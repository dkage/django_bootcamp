from django.shortcuts import render
import django.utils.timezone as tz
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import *


# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=tz.now().order_by('-published_date'))


class PostDetailView(DetailView):
    model = Post

