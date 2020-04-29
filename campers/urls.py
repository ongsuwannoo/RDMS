from django.urls import path

from . import views

urlpatterns = [
    path('', views.campers, name='campers'),
    path('create_camper/', views.create_camper, name='create_camper'),
    path('<int:id_camper>/', views.camper_detail, name='camper_detail'),
    path('<int:id_camper>/add_observe', views.add_observe, name='add_observe'),
    path('delete_camper/<int:id_camper>/', views.delete_camper, name='delete_camper'),
    path('<int:id_camper>/edit_camper/', views.edit_camper, name='edit_camper'),
    path('import_camper/', views.import_camper, name='import_camper'),
]
