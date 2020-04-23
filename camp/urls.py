from django.urls import path, include

from . import views

urlpatterns = [
    # /camp/
    path('', views.camp, name='camp'),
    # /camp/1/
    path('<int:id_camp>/', views.camp, name='camp'),
    # /camp/1/campers/
    path('<int:id_camp>/campers/', include('campers.urls')),
    # /flow/1/campers/
    path('<int:id_camp>/flow/', include('flow.urls')),
    # /staffs/1/campers/
    path('<int:id_camp>/staffs/', include('staffs.urls')),

    path('create_camp/', views.create_camp, name='create_camp'),

    path('<int:id_camp>/create_department_mc/', views.create_department_mc, name='create_department_mc'),
    
]
