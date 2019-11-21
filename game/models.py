from django.contrib.auth.models import User
from django.contrib.auth import *
from django.db import models

class Knowing(models.Model):
	name = models.CharField(max_length=30)
	force = models. IntegerField(default=0)
	defense = models.IntegerField(default=0)
	allowed_level = models.IntegerField(default=0)
	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=40)
	force = models. IntegerField(default=0)
	defense = models. IntegerField(default=0)
	allowed_level = models. IntegerField(default=0)
	def __str__(self):
		return self.name

class Avatar(models.Model):
	owner = models.OneToOneField('auth.User', related_name='avatar_owner', on_delete=models.CASCADE)
	name = models.CharField(max_length=12)
	force = models. IntegerField(default=100)
	defense = models.IntegerField(default=80)
	life = models.IntegerField(default=1000)
	level = models.IntegerField(default=0)
	knowing = models.ManyToManyField(Knowing)
	item = models.ManyToManyField(Item)
	def __str__(self):
		return self.name

