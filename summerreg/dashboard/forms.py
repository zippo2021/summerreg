# -*- coding: utf-8 -*-
from django import forms
from dashboard.models import UserData,Passport,Zagran,Birth_cert
from django.forms.fields import DateInput
from django.forms.extras.widgets import SelectDateWidget

BIRTH_YEAR_CHOICES = ('1984')
BIRTH_MONTHS_CHOISES = ('1')
BIRTH_DAYS_CHOISES = ('1')
school_choices = (('Школа 1','Школа 1'),('Школа 2','Школа 2'),('Школа 3','Школа 3'))

class UserCreationForm(forms.ModelForm):
    birthdate = forms.DateField(label='Дата рождения',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    school = forms.ChoiceField(choices=school_choices, required = True, label='Школа')
    class Meta:
        model = UserData
        '''fields = [
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
                ]'''
        exclude = [
                  'id',
                  'is_admin',
                  'is_accepted',
                  'is_moderator',
                  'passport',
                  'zagran',
                  'birth_cert',
                  'doc_type',
                ]

class DocSelectForm(forms.Form):
    doc_type = forms.ChoiceField(choices=(('0','Паспорт'),('1','Загранпаспорт'),('2','Свидетельство о рождении')), required = False, label='Выберите тип документа')

class ZagranForm(forms.ModelForm):
    when_issued = forms.DateField(label='Когда выдан',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))        
    class Meta:
        model = Zagran

class PassportForm(forms.ModelForm):
    when_issued = forms.DateField(label='Когда выдан',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    class Meta:
        model = Passport

class BirthCertForm(forms.ModelForm):
    when_issued = forms.DateField(label='Когда выдан',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    class Meta:
        model = Birth_cert
