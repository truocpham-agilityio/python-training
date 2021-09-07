from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('forms/', views.forms, name='form'),
]
