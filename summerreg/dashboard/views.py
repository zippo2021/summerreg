from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from dashboard.forms import UserCreationForm
from dashboard.models import UserData

def create_data_model(form,id):
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            id = request.user
            data = create_data_model(form,id)
            data.save()
            '''form.(initial={'id') = id
            form.save();''' 
            return redirect('dash_index')               
        else:
            html = render(request,"dashboard/summer_registration_form.html",{'form':form})
            return HttpResponse(html)
    else:        
        form = UserCreationForm()        
        html = render(request,"dashboard/summer_registration_form.html",{'form':form})    
        return HttpResponse(html)   
      
@login_required
def user_data_viewer(request):
    id = request.user    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)    
        if form.is_valid():
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
    

