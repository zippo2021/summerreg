# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Passport(models.Model):
    ser = models.PositiveIntegerField(verbose_name='Серия',max_length=4)
    number = models.PositiveIntegerField(verbose_name='Номер',max_length=6)
    issued_by = models.CharField(verbose_name="Кем выдан",max_length=255)
    when_issued = models.DateField(verbose_name="Когда выдан")
    code = models.CharField(verbose_name="Код подразделения",max_length=30)
    
class Birth_cert(models.Model):
    ser = models.PositiveIntegerField(verbose_name='Серия',max_length=4)
    number = models.PositiveIntegerField(verbose_name='Номер',max_length=6)
    issued_by = models.CharField(verbose_name="Кем выдано",max_length=255)  
    when_issued = models.DateField(verbose_name="Когда выдано") 

class Zagran(models.Model):
    ser = models.PositiveIntegerField(verbose_name='Серия',max_length=2)
    number = models.PositiveIntegerField(verbose_name='Номер',max_length=7)
    issued_by = models.CharField(verbose_name="Кем выдан",max_length=255)
    when_issued = models.DateField(verbose_name="Когда выдан")
    exp_date = models.DateField(verbose_name="Срок действия")

class UserData(models.Model):
    id = models.OneToOneField(User,primary_key=True)
    avatar = models.ImageField(verbose_name='Аватар',  upload_to='images/profile_pics', blank=True, null=True)
    first_name = models.CharField(verbose_name='Имя',  max_length=255)
    middle_name = models.CharField(verbose_name='Отчество',  max_length=255,blank=True)
    last_name = models.CharField(verbose_name='Фамилия',  max_length=255)
    birthdate = models.DateField(verbose_name='Дата рождения',null=True)
    birthplace = models.CharField(verbose_name='Место рождения',  max_length=255)
    postal_code = models.PositiveIntegerField(verbose_name='Почтовый индекс',max_length=6)
    city = models.CharField(verbose_name='Город',  max_length=255)
    street = models.CharField(verbose_name='Улица',  max_length=255) 
    building = models.PositiveIntegerField(verbose_name='Дом',  max_length=4)
    housing = models.PositiveIntegerField(verbose_name='Корпус',  max_length=2)
    appartment = models.PositiveIntegerField(verbose_name='Квартира',  max_length=5)
    doc_type = models.PositiveIntegerField(verbose_name='Тип документа',max_length=1,null=True)
    passport = models.OneToOneField(Passport,null=True)
    zagran = models.OneToOneField(Zagran,null=True)
    birth_cert = models.OneToOneField(Birth_cert,null=True)
    is_admin = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    

    
    
