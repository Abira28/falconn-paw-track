from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pets/', views.pet_list, name='pet_list'),
    path('owners/', views.owner_list, name='owner_list'),
]