# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from ConfigParser import RawConfigParser
from django.contrib.admin.views.decorators import staff_member_required
import os


config = RawConfigParser()
config_file = open(os.path.join(os.getcwd(),'config.cfg'))
config.readfp(config_file)

@staff_member_required
def index(request):
    template = loader.get_template('export/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

@staff_member_required
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

@staff_member_required
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

@staff_member_required
def create(request):
    from export.forms import showdb_form
    if request.method == 'POST':
	form = showdb_form(request.POST)
    	if form.is_valid():
	    request.session['form_data']=form.cleaned_data
	    return redirect('results')
    else:
	form = showdb_form()
    template = loader.get_template('export/create.html')
    context = RequestContext(request, {'form' : form})
    return HttpResponse(template.render(context)) 

def create_table(cleaned_data):
    from dashboard.models import UserData
    fields = config.get('Export','fields_to_show').split(', ')
    #about cities
    if 'Все' in cleaned_data['cities']:
	    filter_cities = False
    else:
        filter_cities = True
	cities = cleaned_data['cities']
    #about is_accepted
    filter_accepted = cleaned_data['accepted'] == 'not'
    #executing
    filtered = UserData.objects.all()
    if filter_cities:
	    filtered = filtered.filter(city__in = cities)
    if filter_accepted:
        filtered = filtered.filter(is_accepted__exact = False)
    table = filtered.values(*fields)
    return table

@staff_member_required
def apply_user(request, id):
    from dashboard.models import UserData
    user = UserData.objects.get(id=id)
    user.is_accepted = not(user.is_accepted)
    user.save()
    return redirect('results')

def results(request):
     cleaned_data = request.session['form_data']
     table = create_table(cleaned_data)
     if not table: no_results = True
     else: no_results = False
     template = loader.get_template('export/results.html')
     context = RequestContext(request, {'table' : table, 'no_results': no_results})
     return HttpResponse(template.render(context))
