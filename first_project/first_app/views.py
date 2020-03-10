from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *


def index(request):

    # Sqlite call in
    web_pages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'access_records': web_pages_list,
    }

    return render(request, 'first_app/index.html', context=date_dict)
