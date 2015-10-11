from django.db import models
from datetime import datetime

# Cal Hacks Fall 2015
# Name: Cal Hacks Team EATR
# Authors: Annie Tsai, Emily Tsai

class List(models.Model):
	name = models.CharField(max_length=250, unique=True)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
	class Admin:
		pass

class Item(models.Model):
	name = models.CharField(max_length=250)
	life = models.IntegerField(default=10)
	date = models.DateTimeField(default=datetime.now)
	completed = models.BooleanField(default=False)
	stock = models.ForeignKey(List)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ["-life", "name"]
	class Admin:
		pass

# PRIORITY_CHOICES = ( 
# 	(1, 'Low'), 
#     (2, 'Normal'), 
#     (3, 'High'), 
# ) 

# class Item(models.Model): 
#     title = models.CharField(maxlength=250) 
#     created_date = models.DateTimeField(default=datetime.now) 
#     priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
#     completed = models.BooleanField(default=False) 
#     todo_list = models.ForeignKey(List) 
#     def __str__(self): 
#         return self.title 
#     class Meta: 
#         ordering = ['-priority', 'title'] 
#     class Admin: 
#         pass