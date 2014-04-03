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
    fields = config.get('Export','fields_to_show')
    #writer.writerow(fields)
    for each in UserData.objects.values_list(): 
        writer.writerow(each)
<<<<<<< HEAD
=======
    field = 'username'
    writer.writerow(field)
    for each in User.objects.values(field): 
        writer.writerow(each.values())
>>>>>>> d0f70ed826569a7946271bb56fb9a94e7b5949d9
    return response

def show_database(request):
    from export.forms import showdb_form
    if request.method == 'POST': form = showdb_form(request.POST)
    else: form = showdb_form()
    template = loader.get_template('export/create.html')
    context = RequestContext(request, {'form' : form})
    return HttpResponse(template.render(context))

def results(request):
    from dashboard.models import UserData
    template = loader.get_template('export/showdb.html')
    #fields = config.get('Export','fields_to_show')
    fields = ('id','is_accepted','last_name','first_name','middle_name','city')
    values = (each for each in UserData.objects.exclude(is_admin='True').values_list(*fields))
    table = dict.fromkeys(fields, values)
    context = RequestContext(request, {'table' : table})
    return HttpResponse(template.render(context))

def apply_user(request, id):
    from dashboard.models import UserData
    user = UserData.objects.get(id=id)
    user.is_applyed = True
    user.save()
    return redirect('showdb')
