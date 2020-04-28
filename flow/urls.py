from django.urls import path

from . import views

urlpatterns = [
    path('', views.flow, name='flow'),
    path('addFlow/', views.addFlow, name='addFlow'),
    
]
