from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from ConfigParser import RawConfigParser
import os

config = RawConfigParser()
config_file = open(os.path.join(os.getcwd(),'config.cfg'))
config.readfp(config_file)


def index(request):
    template = loader.get_template('export/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def export_database(request):
    import os
    from datetime import date
    from django.conf import settings
    db = settings.DATABASES['default']
    cmd = '/usr/bin/mysqldump --opt --compact --skip-add-locks --add-drop-table -u %s -p%s %s | bzip2 -c' % (db['USER'], db['PASSWORD'], db['NAME'])
    stdin, stdout = os.popen2(cmd)
    stdin.close()
    response = HttpResponse(stdout, mimetype="application/octet-stream")
    response['Content-Disposition'] = 'attachment; filename=%s_db.sql.bz2' % date.today()
    return response


def export_csv(request):
    import csv       
    from dashboard.models import UserData
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="db.csv"'
    writer = csv.writer(response)
    fields = config.get('Export','fields_to_csv').split(', ')
    #writer.writerow(fields)
    for each in UserData.objects.values_list(*fields): 
        writer.writerow(each)
    return response

def create(request):
    from export.forms import showdb_form
    if request.method == 'POST':
	form = showdb_form(request.POST)
    	if form.is_valid():
	    table=results(form)			
    	    template = loader.get_template('export/results.html')
	    context = RequestContext(request, {'table' : table})
	    return HttpResponse(template.render(context))
    else:
	form = showdb_form()
    template = loader.get_template('export/create.html')
    context = RequestContext(request, {'form' : form})
    return HttpResponse(template.render(context)) 

def results(form):
    from dashboard.models import UserData
    from export.forms import showdb_form
    fields = config.get('Export','fields_to_show').split(', ')
    #about cities
    if form.cleaned_data['city_all'] == True:
	filter_cities = False
    else:
        filter_cities= True
	cities=[]
	for key in form.cleaned_data.keys():
	    if 'city_' in key: 
		if form.cleaned_data[key] == True:
		    cities.append(key.split('_')[1]) 
    #about is_accepted
    filter_accepted = form.cleaned_data['accepted'] == 'accepted_not'
    #executing
    filtered = UserData.objects.all()
    if filter_cities:
	filtered = filtered.filter(city__in = cities)
    if filter_accepted:
        filtered = filtered.filter(is_accepted__exact = False)
    table = filtered.values(*fields)
    return table

def apply_user(request, id):
    from dashboard.models import UserData
    user = UserData.objects.get(id=id)
    user.is_applyed = True
    user.save()
    return redirect('showdb')
