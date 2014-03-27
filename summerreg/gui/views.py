from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
  t = get_template('gui_index.html')
  html = t.render(Context())
  return HttpResponse(html)

@login_required
def data_load(request):
  t = get_template(data_table.html)
  html = t.render(Context())
  return HttpRespose(html) 
