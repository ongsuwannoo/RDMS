from django.urls import path

from . import views

urlpatterns = [
    path('', views.staffs, name='staffs'),
    path('create_staff/', views.create_staff, name='create_staff'),
    
]
