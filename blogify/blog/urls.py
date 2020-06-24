from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about', views.AboutView, name='about'),

    # Post views
    path('post/<int:pk>', views.PostDetailView, name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
]
