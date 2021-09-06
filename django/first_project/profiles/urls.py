from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.profile_page, name='profile_page'),
]
