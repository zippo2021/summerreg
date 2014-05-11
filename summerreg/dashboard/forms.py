# -*- coding: utf-8 -*-
from django import forms
from dashboard.models import UserData,Passport,Zagran,Birth_cert
from django.forms.fields import DateInput
from django.forms.extras.widgets import SelectDateWidget
from django.core.files.images import get_image_dimensions
from school import school_choices
BIRTH_YEAR_CHOICES = ('1984')
BIRTH_MONTHS_CHOISES = ('1')
BIRTH_DAYS_CHOISES = ('1')


class UserCreationForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар',required=False, error_messages = {'invalid':"Только изображения"}, widget=forms.FileInput)
    birthdate = forms.DateField(label='Дата рождения',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',),help_text="Формат: дд/мм/гггг")
    school = forms.ChoiceField(choices=school_choices, required = True, label='Школа',help_text="Если вашей школы нет в списке, обратитесь к администратору.")  
    parent_1_phone = forms.RegexField(label='Телефон родителя 1',regex=r'^\+?1?\d{11,15}$', 
                                error_message = ("Формат: '+00000000000'."))
    parent_2_phone = forms.RegexField(label='Телефон родителя 2',regex=r'^\+?1?\d{11,15}$', 
                                error_message = ("Формат: '+00000000000'."))
    postal_code = forms.RegexField(label='Почтовый индекс',regex=r'^\d+',error_message = ("Необходимо ввести 6 цифр"))
    building = forms.RegexField(label='Дом',regex=r'^\d+',required=True)
    housing = forms.RegexField(label='Корпус',regex=r'^\d+',required=False)
    appartment = forms.RegexField(label='Квартира',regex=r'^\d+',required=True)
    class Meta:
        model = UserData
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
    when_issued = forms.DateField(label='Когда выдан',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',),help_text="Формат: дд/мм/гггг") 
    exp_date = forms.DateField(label='Срок действия',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',),help_text="Формат: дд/мм/гггг")       
    class Meta:
        model = Zagran
        exclude = ['user']

class PassportForm(forms.ModelForm):
    when_issued = forms.DateField(label='Когда выдан',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',),help_text="Формат: дд/мм/гггг")
    class Meta:
        model = Passport
        exclude = ['user']

class BirthCertForm(forms.ModelForm):
    when_issued = forms.DateField(label='Когда выдано',widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',),help_text="Формат: дд/мм/гггг")
    class Meta:
        model = Birth_cert
        exclude = ['user']
