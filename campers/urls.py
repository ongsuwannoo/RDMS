from django.urls import path

from . import views

urlpatterns = [
    path('', views.campers, name='campers'),
    path('<int:number>/', views.camper_detail, name='camper_detail'),
    
]
