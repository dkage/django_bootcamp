from django.urls import path
from blog.views import *


urlpatterns = [
    path('about', AboutView.as_view(), name='about')
]