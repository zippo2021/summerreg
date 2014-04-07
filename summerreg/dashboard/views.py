from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from dashboard.forms import UserCreationForm,DocSelectForm,PassportForm,ZagranForm,BirthCertForm
from dashboard.models import UserData,Passport,Zagran,Birth_cert

def create_data_model(form,id,avatar):          
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
            try:
                avatar = request.FILES['avatar']
                raise Exception('No file provided')
            except Exception as inst:
                avatar = None
            data = create_data_model(form,id,avatar)
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
            try:
                avatar = request.FILES['avatar']
            except Exception as inst:
                avatar = None
            data = create_data_model(form,id,avatar)
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
    

