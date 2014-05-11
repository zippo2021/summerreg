from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.core.mail import EmailMessage

from dashboard.forms import UserCreationForm,DocSelectForm,PassportForm,ZagranForm,BirthCertForm
from dashboard.models import UserData,Passport,Zagran,Birth_cert

def create_data_model(form,id):          
    data = UserData(id=id,**form.cleaned_data)        
    return data

@login_required
def dash_index(request):
    id = request.user     
    p = False    
    try:
        tmp_data = UserData.objects.get(id=id)
    except UserData.DoesNotExist:
        p = True #No userdata stored, so registration is available       
    html = render(request,"dashboard/dash_index.html",{"reg_permitted":p})
    return HttpResponse(html)

@login_required
def summer_registration(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            id = request.user
            data = create_data_model(form,id)
            data.save() 
            return redirect('doc_type_select')               
        else:
            html = render(request,"dashboard/summer_registration_form.html",{'form':form})
            return HttpResponse(html)
    else:        
        form = UserCreationForm()        
        html = render(request,"dashboard/summer_registration_form.html",{'form':form})    
        return HttpResponse(html)   

@login_required
def doc_type_select(request):
    if request.method == 'POST':
        form = DocSelectForm(request.POST)
        if form.is_valid():
            data = UserData.objects.get(id=request.user)
            doctype = form.cleaned_data['doc_type']   
            data.doc_type = doctype
            data.save()
            request.session['doctype'] = doctype
            return redirect('doc_info')
    else:
        form = DocSelectForm()
        html = render(request,"dashboard/doc_type_select.html",{'form':form})
        return HttpResponse(html)

def document_create(data,form,doctype):
    if doctype=='0':
        document = Passport(user=data,**form.cleaned_data)
    elif doctype=='1':
        document = Zagran(user=data,**form.cleaned_data)
    elif doctype=='2':
        document = Birth_cert(user=data,**form.cleaned_data)
    else:
        document = Passport(user=data,**form.cleaned_data)
    return document

@login_required
def doc_info(request): 
    data = UserData.objects.get(id=request.user)   
    doctype = data.doc_type
    if doctype=='0':
        form = PassportForm(request.POST or None)
    elif doctype=='1':
        form = ZagranForm(request.POST or None)
    elif doctype=='2':
        form = BirthCertForm(request.POST or None)   
    else:
        form = PassportForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():                       
            document = document_create(data,form,doctype)
            document.save()
            return redirect('dash_index')
        else:
            html = render(request,"dashboard/doc_info_form.html",{'form':form})
            return HttpResponse(html)    
    else:
        html = render(request,"dashboard/doc_info_form.html",{'form':form})
        return HttpResponse(html)

@login_required
def user_data_viewer(request):
    id = request.user    
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)    
        if form.is_valid():
            print form.cleaned_data['avatar']
            data = create_data_model(form,id)
            data.save()
            return redirect('dash_index')
        else:
            html = render(request,"dashboard/summer_registration_form.html",{'form':form})
            return HttpResponse(html)
    else:    
        try:
            tmp_data = UserData.objects.get(id=id)
        except UserData.DoesNotExist:            
            form = UserCreationForm()    
            html = render(request,"dashboard/worksheet.html",{'form':form})
            return HttpResponse(html)        
        form = UserCreationForm(instance=tmp_data)    
        html = render(request,"dashboard/worksheet.html",{'form':form})
        return HttpResponse(html)
    
@login_required
def user_events_main(request):
    from dashboard.models import Event
    user_id = request.user.id
    events = Event.objects.all()
    other = events.exclude(requests__id = user_id).exclude(participants__id = user_id)
    requested = events.filter(requests__id = user_id)
    applied = events.filter(participants__id = user_id)
    html = render(request, "dashboard/user_events_main.html", {'events_requested':requested, 'events_applied':applied, 'events_other':other, 'id':user_id})
    return HttpResponse(html)

@login_required
def user_events_request(request, event_id):
    from dashboard.models import Event
    event = Event.objects.get(id=event_id)
    user_id = request.user
    user = UserData.objects.get(id=user_id)
    event.requests.add(user)
    return redirect('user_events_main')

@login_required
def user_events_undo(request, event_id):
    from dashboard.models import Event
    event = Event.objects.get(id=event_id)
    user_id = request.user
    user = UserData.objects.get(id=user_id)
    event.requests.remove(user)
    return redirect('user_events_main')

@staff_member_required
def admin_events_show(request, event_id):
    from dashboard.models import Event
    event = Event.objects.get(id=event_id)
    html = render(request,"dashboard/admin_events_show.html", {"event":event})
    return HttpResponse(html)

@staff_member_required
def admin_events_main(request):
    from dashboard.models import Event
    events = Event.objects.all()
    html = render(request, "dashboard/admin_events_main.html", {'events':events})
    return HttpResponse(html)

@staff_member_required
def admin_events_apply(request, event_id, user_id):
    from dashboard.models import Event
    event = Event.objects.get(id=event_id)
    user = UserData.objects.get(id=user_id)
    mail = EmailMessage('Подтверждение заявки', message, settings.EMAIL_HOST_USER, [user.])
    event.requests.remove(user)
    event.participants.add(user)
    return redirect('admin_events_show', event_id)

@staff_member_required
def admin_events_disapply(request, event_id, user_id):
    from dashboard.models import Event
    event = Event.objects.get(id=event_id)
    user = UserData.objects.get(id=user_id)
    event.participants.remove(user)
    event.requests.remove(user)
    return redirect('admin_events_show', event_id)

@staff_member_required
def view_profile(request):
    uid = request.GET.get('uid','')
    userdata = UserData.objects.get(id=uid)
    context = userdata.__dict__
    html = render(request, "dashboard/user_profile.html",context)
    return HttpResponse(html)


