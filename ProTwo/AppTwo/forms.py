from django import forms
from django.core import validators
from .models import *


class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
