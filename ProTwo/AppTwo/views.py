from django.shortcuts import render
from django.http import HttpResponse


# Views
def index(request):
    return render(request, 'AppTwo/index.html')


def help_page(request):
    return_dict = {'help_message': 'HELP WEB PAGE'}
    return render(request, 'AppTwo/help.html', context=return_dict)
