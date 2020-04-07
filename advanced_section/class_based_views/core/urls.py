from django.urls import path
from .views import *


# App namespace name
app_name = 'local_core'

# URLs
urlpatterns = [
    path('', SchoolListView.as_view(), name='list'),
    path('detail_<slug:slug>/', SchoolDetailView.as_view(), name='detail')
]
