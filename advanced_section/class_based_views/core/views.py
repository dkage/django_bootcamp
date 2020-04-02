from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import *


class CBView(View):

    def get(self, request):
        return HttpResponse("Class based views!")


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['variable'] = 'Hello string'

        return context


class SchoolListView(ListView):
    model = School


class SchoolDetailView(DetailView):
    model = School
    template_name = 'core_base.html'
