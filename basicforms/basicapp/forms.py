from tkinter.tix import Form
from django import forms


class FormUser (forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    # Email field requires a @, and a ".something" suffix, or else the is_valid method returns false
    email = forms.EmailField()


