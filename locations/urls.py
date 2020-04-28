from django.urls import path

from . import views

urlpatterns = [
    path('', views.locations, name='locations'),
    path('create_location/', views.create_location, name='create_location'),
    path('update_location/', views.update_location, name='update_location'),
]
