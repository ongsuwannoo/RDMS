from django.urls import path

from . import views

urlpatterns = [
    path('', views.campers, name='campers'),
    path('create_camper/', views.create_camper, name='create_camper'),
    path('<int:id_camper>/', views.camper_detail, name='camper_detail'),
    
]
