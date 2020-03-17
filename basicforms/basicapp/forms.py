from tkinter.tix import Form
from django import forms


class FormUser (forms.Form):
    name = forms.CharField()
    email = forms.EmailField()  # # Email field requires a @, and a ".something" suffix to pass is_valid() function
    text = forms.CharField(widget=forms.Textarea)


    # Security variable
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_bot_catcher(self):
        bot_catcher = self.cleaned_data['bot_catcher']

        if len(bot_catcher) > 0:
            raise forms.ValidationError("Bot behavior detected.")

