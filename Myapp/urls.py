from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('FindDisease', views.fDisease, name="FindDisease"),
    path('AboutDisease', views.aDisease, name="AboutDisease"),
    path('FindDoctor', views.fDoctor, name="FindDoctor"),
    path('FindHospital', views.fHospital, name="FindHospital"),
    path('Searched', views.searched, name="Searched"),
    path('Details', views.details, name="Details"),
    path('Dfinded', views.dfinded, name="Dfinded"),
    path('Hfinded', views.hfinded, name="Hfinded"),
    path('not', views.notfind, name='not find'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('regd', views.regd),
    path('sorry', views.sorry),
    path('login', views.login),
    path('admin_login', views.admin_login),
    path('Show_disease', views.show_disease),
    path('Insert_disease', views.Insert_disease),
    path('Disease_inserted', views.diseaseInserted),
    path('Already', views.already),
    path('Admin',views.Admin),
    path('Show_doctors', views.Show_doctors),
    path('Insert_doctor', views.Insert_doctor),
    path('Doctor_inserted', views.Doctor_inserted),
    path('Show_hospitals', views.Show_hospitals),
    path('Insert_hospital', views.Insert_hospital),
    path('Hospital_inserted', views.Hospital_inserted),
    path('show_users', views.show_users),
    path('logged_admin', views.logged_admin),



]
