from django.urls import path

from . import views, site_views

urlpatterns = [
    path('', site_views.home, name='home'),
    path('about/', site_views.about, name='about'),
    path('services/', site_views.services, name='services'),
    path('contact/', site_views.contact, name='contact'),
    path('book/', site_views.book, name='book'),
    path('thanks/', site_views.thanks, name='thanks'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pets/', views.pet_list, name='pet_list'),
    path('owners/', views.owner_list, name='owner_list'),
]
