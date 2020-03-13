from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User


def index(request):
    return render(request, 'index.html')


def users(request):
    # List users saved at database

    users_list = User.objects.order_by("last_name")

    # Every context args for render should be in a single dict, those are then iterated inside template
    context_dicts = {
        "users_list": users_list
    }

    return render(request, 'users.html', context=context_dicts)

