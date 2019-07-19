from django.urls import path, include 
from django.conf.urls import url

from . import views
# the following line is not needed since i am using all views in the line above
# from dash.views import causelossModelForm, causelossModelForm2, causelossdetail

urlpatterns = [
    path('students/', views.add_student, name='dash-home'),
]