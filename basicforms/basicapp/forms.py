from tkinter.tix import Form

from django import forms


class FormTest (forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


