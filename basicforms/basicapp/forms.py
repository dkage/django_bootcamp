from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with letter 'Z'.")


class FormUser (forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()  # # Email field requires a @, and a ".something" suffix to pass is_valid() function
    email_verify = forms.EmailField(label='Enter your e-mail again')
    text = forms.CharField(widget=forms.Textarea)

    # Security variable
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super(FormUser, self).clean()
        email = all_clean_data['email']
        email_v = all_clean_data['email_verify']

        if email != email_v:
            raise forms.ValidationError("E-mails doesn't match!")
