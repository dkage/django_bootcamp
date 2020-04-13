from django.urls import path
from blog.views import *


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('about', AboutView.as_view(), name='about'),
    path('post/<slug:slug>', DetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
]
