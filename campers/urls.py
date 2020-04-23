from django.urls import path

from . import views

urlpatterns = [
    path('', views.campers, name='campers'),
    path('<int:id_camp>/', views.camper_detail, name='camper_detail'),
    
]
