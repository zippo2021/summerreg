# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    id = models.OneToOneField(User,primary_key=True)
    avatar = models.ImageField(verbose_name='Аватар',  upload_to='images/profile_pics',blank=True,null=True)
    first_name = models.CharField(verbose_name='Имя',  max_length=255)
    middle_name = models.CharField(verbose_name='Отчество',  max_length=255,blank=True,null=True)
    last_name = models.CharField(verbose_name='Фамилия',  max_length=255)
    birthdate = models.DateField(verbose_name='Дата рождения',null=True)
    birthplace = models.CharField(verbose_name='Место рождения',  max_length=255)
    postal_code = models.CharField(verbose_name='Почтовый индекс',max_length=6)
    city = models.CharField(verbose_name='Город',  max_length=255)
    street = models.CharField(verbose_name='Улица',  max_length=255) 
    building = models.CharField(verbose_name='Дом',  max_length=4,null=True,blank=True)
    housing = models.CharField(verbose_name='Корпус',  max_length=2)
    appartment = models.CharField(verbose_name='Квартира',  max_length=5)
    parent_1 = models.CharField(verbose_name='Фамилия Имя Отчество родителя 1',  max_length=255)
    parent_1_phone  = models.CharField(verbose_name='Телефон родителя 1',max_length=15)  
    parent_2 = models.CharField(verbose_name='Фамилия Имя Отчество родителя 2',  max_length=255,blank=True, null=True)
    parent_2_phone = models.CharField(verbose_name='Телефон родителя 2',max_length=15,blank=True, null=True)
    school = models.CharField(verbose_name='Школа',  max_length=255)
    phys_teacher_initial = models.CharField(verbose_name='Фамилия Имя Отчество учителя физики',  max_length=255)
    maths_teacher_initial = models.CharField(verbose_name='Фамилия Имя Отчество учителя математики',  max_length=255)
    principle_initial = models.CharField(verbose_name='Фамилия Имя Отчество директора школы',  max_length=255)
    doc_type = models.CharField(verbose_name='Тип документа',max_length=1,default='0')
    is_admin = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)

class Passport(models.Model):
    user = models.OneToOneField(UserData,primary_key=True)
    ser = models.PositiveIntegerField(verbose_name='Серия',max_length=4)
    number = models.PositiveIntegerField(verbose_name='Номер',max_length=6)
    issued_by = models.CharField(verbose_name="Кем выдан",max_length=255,)
    when_issued = models.DateField(verbose_name="Когда выдан")
    code = models.CharField(verbose_name="Код подразделения",max_length=30)
    
class Birth_cert(models.Model):
    user = models.OneToOneField(UserData,primary_key=True)
    ser = models.PositiveIntegerField(verbose_name='Серия',max_length=4)
    number = models.PositiveIntegerField(verbose_name='Номер',max_length=6)
    issued_by = models.CharField(verbose_name="Кем выдано",max_length=255)  
    when_issued = models.DateField(verbose_name="Когда выдано") 

class Zagran(models.Model):
    user = models.OneToOneField(UserData,primary_key=True)
    ser = models.PositiveIntegerField(verbose_name='Серия',max_length=2)
    number = models.PositiveIntegerField(verbose_name='Номер',max_length=7)
    issued_by = models.CharField(verbose_name="Кем выдан",max_length=255)
    when_issued = models.DateField(verbose_name="Когда выдан")
    exp_date = models.DateField(verbose_name="Срок действия")

class Event(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    issued = models.DateField(verbose_name="Содано")
    closed = models.DateField(verbose_name="Закрыто")
    requests = models.ManyToManyField(UserData, blank=True, related_name="requests")
    participants = models.ManyToManyField(UserData, blank=True, related_name="participants")     
