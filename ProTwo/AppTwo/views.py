from django.shortcuts import render
from django.http import HttpResponse


# Views
def index(request):
    return HttpResponse("<em>My Second App</em>")