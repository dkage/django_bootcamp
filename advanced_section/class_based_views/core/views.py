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
    context_object_name = 'schools'
    model = School
    template_name = 'school_list.html'


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'school_detail.html'
    slug_field = 'id'
