# import re
# from django import forms
# from .models import *
# from django.contrib.auth.models import User

# class AddItem(forms.ModelForm):

# 	item = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=50, render_value=False)), label=_("New Item"))
# 	life = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=3, render_value=False)), label=_("Shelf Life"))

# 	def add_to_list(self):
# 		Item('item', 'life', List("Grocery List"))