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
    from django.contrib.auth.models import User
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="db.csv"'
    writer = csv.writer(response)
    fields = config.get('Export','fields_to_show')
    #writer.writerow(fields)
    for each in User.objects.values_list(fields): 
        writer.writerow(each)
    field = 'username'
    writer.writerow(field)
    for each in User.objects.values(field): 
        writer.writerow(each.values())
    return response

def show_database(request):
    from django.contrib.auth.models import User
    template = loader.get_template('export/showdb.html')
    fields = config.get('Export','fields_to_show')
    table = [each for each in User.objects.values_list(fields)]
    context = RequestContext(request, {'table' : table})
    return HttpResponse(template.render(context))

def apply_user(request, username):
    from django.contrib.auth.models import User
    user=User.objects.get(username=username)
    user.username+='1'
    user.save()
    return redirect('showdb')
