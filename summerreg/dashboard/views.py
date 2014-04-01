from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from dashboard.forms import UserCreationForm
from dashboard.models import UserData

@login_required
def dash_index(request):
    html = render(request,"dashboard/dash_index.html")
    return HttpResponse(html)

@login_required
def summer_registration(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            id = request.user
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
            data.save()
            '''form.cleaned_data['id'] = id
            form.save();''' 
            return redirect('dash_index')               
        else:
            html = render(request,"dashboard/summer_registration_form.html",{'form':form})
            return HttpResponse(html)
    else:        
        form = UserCreationForm()        
        html = render(request,"dashboard/summer_registration_form.html",{'form':form})    
        return HttpResponse(html)   
      


