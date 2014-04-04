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
<<<<<<< HEAD
=======
    field = 'username'
    writer.writerow(field)
    for each in User.objects.values(field): 
        writer.writerow(each.values())
>>>>>>> 6fe9c8b92004d15a38b1665741779972b9ff75a5
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
    if 'all' in form.cleaned_data['cities']:
	filter_cities = False
    else:
        filter_cities= True
	cities=form.cleaned_data['cities']
    #about is_accepted
    filter_accepted = form.cleaned_data['accepted'] == 'not'
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
    user.is_accepted = True
    user.save()
    return redirect('showdb')
