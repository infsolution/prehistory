from django.contrib.auth.models import User
from django.contrib.auth import *
from django.db import models

class Avatar(models.Model):
	owner = models.OneToOneField('auth.User', related_name='avatar_owner', on_delete=models.CASCADE)
	name = models.CharField(max_length=12)
	force = models. IntegerField(default=100)
	defense = models.IntegerField(default=80)
	life = models.IntegerField(default=1000)
	level = models.IntegerField(default=0)

class Abiliity(models.Model):
	name = models.CharField(max_length=30)
	force = models. IntegerField(default=0)
	allowed_level = models.IntegerField(default=0)
	avatar = models.ManyToManyField(Avatar)

class Knowing(models.Model):
	name = models.CharField(max_length=30)
	defense = models.IntegerField(default=0)
	allowed_level = models.IntegerField(default=0)
	avatar = models.ManyToManyField(Avatar)