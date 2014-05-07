# -*- coding: utf-8 -*-
from django import forms
from dashboard.models import UserData


class showdb_form(forms.Form):
    #dynamic form, fields: checkboxes 
    CITY_CHOICES = ['All']+list(set(UserData.objects.values_list('city', flat = True)))
    CITY_CHOICES = [(each, each) for each in CITY_CHOICES]
    cities = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=CITY_CHOICES, label='Cities(to be trans)')

    #dynamic form, static fields
    accepted = forms.ChoiceField(choices=(('all','Все'),('not','Только не принятые')), required = False, label='Users(to be trans)')
    #special
    def get_city_choices():
	    return CITY_CHOICES[:].remove('All')
    
