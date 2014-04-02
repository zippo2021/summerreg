# -*- coding: utf-8 -*-
from django import forms
from dashboard.models import UserData
from django.forms.fields import DateInput
from django.forms.extras.widgets import SelectDateWidget

BIRTH_YEAR_CHOICES = ('1984')
BIRTH_MONTHS_CHOISES = ('1')
BIRTH_DAYS_CHOISES = ('1')
class UserCreationForm(forms.ModelForm):
    #avatar  = forms.FileField(label = 'Аватар')
    birthdate = forms.DateField(label='Дата рождения',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    class Meta:
        model = UserData
        fields = [
                    'first_name',
                    'middle_name',
                    'last_name', 
                    'birthdate',
                    'birthplace',
                    'postal_code',
                    'city',
                    'street',
                    'building',
                    'housing',
                    'appartment',                    
                ]
