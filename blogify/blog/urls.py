from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about', views.AboutView, name='about'),
    path('post/<int:pk>', views.PostDetailView),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),

]
