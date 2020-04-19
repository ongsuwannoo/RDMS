from django.urls import path, include

from . import views

urlpatterns = [
    # /camp/
    path('', views.camp, name='camp'),
    # /camp/1/
    path('<int:number>/', views.camp, name='camp'),
    # /camp/1/campers/
    path('<int:number>/campers/', include('campers.urls')),
    # /flow/1/campers/
    path('<int:number>/flow/', include('flow.urls')),
    # /staffs/1/campers/
    path('<int:number>/staffs/', include('staffs.urls')),

    path('create_camp/', views.create_camp, name='create_camp'),
    
]
