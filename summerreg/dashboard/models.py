# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    id = models.OneToOneField(User,primary_key=True)
    avatar = models.ImageField(verbose_name='Аватар',  upload_to='images/%Y/%m/%d', blank=True, null=True)
    first_name = models.CharField(verbose_name='Имя',  max_length=255, blank=True)
    middle_name = models.CharField(verbose_name='Отчество',  max_length=255, blank=True)
    last_name = models.CharField(verbose_name='Фамилия',  max_length=255, blank=True)
    birthdate = models.DateField(verbose_name='День рождения',  blank=True, null=True)
    birthplace = models.CharField(verbose_name='Место рождения',  max_length=255, blank=True)
    postal_code = models.DecimalField(verbose_name='Почтовый индекс', max_digits=6,decimal_places=0,blank=True)
    city = models.CharField(verbose_name='Город',  max_length=255, blank=True)
    street = models.CharField(verbose_name='Улица',  max_length=255, blank=True) 
    building = models.DecimalField(verbose_name='Дом',  max_digits=4,decimal_places=0,blank=True)
    housing = models.DecimalField(verbose_name='Корпус',  max_digits=2,decimal_places=0,blank=True)
    appartment = models.DecimalField(verbose_name='Квартира',  max_digits=5,decimal_places=0,blank=True)
    is_admin = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    