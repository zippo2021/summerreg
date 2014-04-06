from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from dashboard.forms import UserCreationForm,DocSelectForm,PassportForm,ZagranForm,BirthCertForm
from dashboard.models import UserData

def create_data_model(form,id,avatar):
    first_name = form.cleaned_data.get('first_name',None)
    middle_name = form.cleaned_data.get('middle_name',None)
    last_name = form.cleaned_data.get('last_name',None)
    birthdate = form.cleaned_data.get('birthdate',None)
    birthplace = form.cleaned_data.get('birthplace',None)
    postal_code = form.cleaned_data.get('postal_code',None)
    city= form.cleaned_data.get('city',None)
    street = form.cleaned_data.get('street',None)
    building = form.cleaned_data.get('building',None)
    housing = form.cleaned_data.get('housing',None)
    appartment = form.cleaned_data.get('appartment',None)            
    data = UserData(
                    id=id,
                    avatar=avatar,
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    birthdate=birthdate,
                    birthplace=birthplace,
                    postal_code=postal_code,
                    city=city,
                    street=street,
                    building=building,
                    housing=housing,
                    appartment=appartment,
                    )        
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
            doctype = form.cleaned_data.get('doc_type',None)            
            data.doctype = doctype
            data.save()
            request.session['doctype'] = doctype
            return redirect('doc_info')
    else:
        form = DocSelectForm()
        html = render(request,"dashboard/doc_type_select.html",{'form':form})
        return HttpResponse(html)

@login_required
def doc_info(request):
    doctype = request.session['doctype']     
    if doctype==0:
        form = PassportForm(request.POST or None)
    elif doctype==1:
        form = ZagranForm(request.POST or None)
    elif doctype==2:
        form = BirthCertForm(request.POST or None)   
    else:
        form = PassportForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
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
    

