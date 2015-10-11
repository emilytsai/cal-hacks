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
	life = models.PositiveIntegerField()
	date = models.DateTimeField(default=datetime.now)
	completed = models.BooleanField(default=False)
	stock = models.ForeignKey(List)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ["-life", "name"]
	class Admin:
		pass