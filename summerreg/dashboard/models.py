# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    id = models.OneToOneField(User,primary_key=True)
    avatar = models.ImageField(verbose_name='Аватар',  upload_to='images/%Y/%m/%d', blank=True, null=True)
    first_name = models.CharField(verbose_name='Имя',  max_length=255)
    middle_name = models.CharField(verbose_name='Отчество',  max_length=255,blank=True)
    last_name = models.CharField(verbose_name='Фамилия',  max_length=255)
    birthdate = models.DateField(verbose_name='День рождения',null=True)
    birthplace = models.CharField(verbose_name='Место рождения',  max_length=255)
    postal_code = models.IntegerField(verbose_name='Почтовый индекс',max_length=6)
    city = models.CharField(verbose_name='Город',  max_length=255)
    street = models.CharField(verbose_name='Улица',  max_length=255) 
    building = models.IntegerField(verbose_name='Дом',  max_length=4)
    housing = models.IntegerField(verbose_name='Корпус',  max_length=2)
    appartment = models.IntegerField(verbose_name='Квартира',  max_length=5)
    is_admin = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    
