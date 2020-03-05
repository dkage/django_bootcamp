from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    test_dict = {'insert_var': 'Hello World Django Template Language'}
    return render(request, 'first_app/index.html', context=test_dict)
