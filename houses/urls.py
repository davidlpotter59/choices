from django.urls import path, include 
from django.conf.urls import url

from . import views

urlpatterns = [
    path('house/', views.add_house, name='house-add'),
]