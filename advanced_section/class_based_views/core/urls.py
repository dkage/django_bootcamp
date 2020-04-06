from django.urls import path
from .views import *


# App namespace name
app_name = 'local_core'

# URLs
urlpatterns = [
    path('', SchoolListView.as_view(), name='list'),
    path('detail_<slug:slug>/', SchoolDetailView.as_view(), name='detail'),
    path('add_school', SchoolCreateView.as_view(), name='add_school'),
    path('update_<slug:pk>', SchoolUpdateView.as_view(), name='update_school'),
    path('delete_<slug:pk>', SchoolDeleteView.as_view(), name='delete_school'),
]
