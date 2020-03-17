from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')


def form_user_view(request):

    if request.method == 'POST':
        form = forms.FormUser(request.POST)
        print("Received POST")
        print(form.is_valid())

        if form.is_valid():
            print("Success POST sent")
            print("Name field received: " + form.cleaned_data['name'])
            print("E-mail address received: " + form.cleaned_data['email'])
            print("Text area received: " + form.cleaned_data['text'])
        else:
            # Create UL with errors in form. Should be returned in response to print for user
            print(form.errors)
    else:
        form = forms.FormUser()

    return render(request, 'basicapp/form_page.html', {'form': form})

