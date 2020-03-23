from django.urls import path
from core import views


# TEMPLATE TAGGING
app_name = 'core'

urlpatterns = [
    path('relative', views.relative, name='relative'),
    path('other', views.other, name='other')
]
