from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.camp, name='camp'),
    path('campers/', include('campers.urls')),
    path('flow/', include('flow.urls')),
    path('staffs/', include('staffs.urls')),
    path('create_camp/', views.create_camp, name='create_camp'),
    path('<camp>/', views.camp, name='camp'),
]
