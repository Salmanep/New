from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home'),
    path('FindDisease', views.fDisease, name="FindDisease"),
    path('AboutDisease', views.aDisease, name="AboutDisease"),
    path('FindDoctor', views.fDoctor, name="FindDoctor"),
    path('FindHospital', views.fHospital, name="FindHospital"),
    path('Searched', views.searched, name="Searched"),
    path('Details', views.details, name="Details"),
    path('Dfinded', views.dfinded, name="Dfinded"),
    path('Hfinded', views.hfinded, name="Hfinded"),
    path('not', views.notfind, name='not find'),

]
