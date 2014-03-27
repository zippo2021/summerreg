from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

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
    import MySQLdb
    from MySQLdb import cursors
    # Needs to be changed-------------------------------------------
    user_name = request.POST.get('user_name', False)
    #---------------------------------------------------------------
    conn = MySQLdb.connect(
    user="user",
    passwd="password",
    db="contrib",
    cursorclass = cursors.SSCursor                                                  )
    cur = conn.cursor()
    print "Executing query"
    # Needs to be changed-------------------------------------------
    if user_name:                                         
	cur.execute("SELECT * FROM auth_user WHERE	  						username = (%s)", (user_name,))
    else:
	cur.execute("SELECT * FROM auth_user")
    # --------------------------------------------------------------
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="db.csv"'
    writer = csv.writer(response) 
    row = cur.fetchone() 
    while row is not None: 
        writer.writerow(row[2:5])
        row = cur.fetchone()
    return response
