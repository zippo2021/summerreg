from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


def index(request):
  
  if request.user.is_authenticated():
    t = get_template('gui_index.html')
    html = t.render(Context())
    return HttpResponse(html)
  else:
    return redirect('/accounts/login')
def data_load(request):

  
  t = get_template(data_table.html)
  html = t.render(Context())
  return HttpRespose(html) 
