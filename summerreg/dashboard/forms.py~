# -*- coding: utf-8 -*-
from django import forms
from dashboard.models import UserData,Passport,Zagran,Birth_cert
from django.forms.fields import DateInput
from django.forms.extras.widgets import SelectDateWidget
from django.core.files.images import get_image_dimensions

BIRTH_YEAR_CHOICES = ('1984')
BIRTH_MONTHS_CHOISES = ('1')
BIRTH_DAYS_CHOISES = ('1')
school_choices = (('Школа 1','Школа 1'),('Школа 2','Школа 2'),('Школа 3','Школа 3'))

class UserCreationForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар',required=True, error_messages = {'invalid':"Только изображения"}, widget=forms.FileInput)
    birthdate = forms.DateField(label='Дата рождения',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    school = forms.ChoiceField(choices=school_choices, required = True, label='Школа')  
    parent_1_phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Формат: '+00000000000'."))
    parent_2_phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Формат: '+00000000000'."))
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
    def clean_avatar(self):
        # получаем данные из нужного поля
        picture =  self.cleaned_data['avatar']
        if picture:
            try:
                # првряем размеры изображения
                # получаем размеры загружаемого изображения
                w, h = get_image_dimensions(picture)

                # задаем ограничения размеров
                max_width = 200 
                max_height = 300 

                # собственно сравнение
                if w > max_width or h > max_height:
                    raise forms.ValidationError(u'Максимальный размер изображения %s x %s пикселов.' % (max_height, max_width))

                # не пропускаем файлы, размер (вес) которых более 100 килобайт
                if len(picture) > (500 * 1024):
                    raise forms.ValidationError(u'Размер изображения не может превышать 500 кб.')

            except AttributeError:
                pass
            return picture

class DocSelectForm(forms.Form):
    doc_type = forms.ChoiceField(choices=(('0','Паспорт'),('1','Загранпаспорт'),('2','Свидетельство о рождении')), required = False, label='Выберите тип документа')

class ZagranForm(forms.ModelForm):
    when_issued = forms.DateField(label='Когда выдан',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',)) 
    forms.DateField(label='Срок действия',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))       
    class Meta:
        model = Zagran
        exclude = ['user']

class PassportForm(forms.ModelForm):
    when_issued = forms.DateField(label='Когда выдан',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    class Meta:
        model = Passport
        exclude = ['user']

class BirthCertForm(forms.ModelForm):
    when_issued = forms.DateField(label='Когда выдано',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    class Meta:
        model = Birth_cert
        exclude = ['user']
