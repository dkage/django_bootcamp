from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User


def index(request):
    return render(request, 'index.html')


def users(request):
    users_list = User.objects.order_by("first_name")
    context_dicts = {
        "users_list": users_list
    }

    return render(request, 'users.html', context=context_dicts)

