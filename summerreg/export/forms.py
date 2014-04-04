from django import forms
from dashboard.models import UserData


class showdb_form(forms.Form):
    #dynamic form, fields: checkboxes 
    CITY_CHOICES = list(UserData.objects.values_list('city', flat = True))+['all']
    CITY_CHOICES = [(each, each) for each in CITY_CHOICES]
    cities = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=CITY_CHOICES, initial='all', label='Cities(to be trans)')

    #dynamic form, static fields
    accepted = forms.ChoiceField(choices=(('all','all'),('not','not applyed')), required = False, label='Users(to be trans)')
    #special
    def get_city_choices():
	return CITY_CHOICES[:].remove('all')
    
