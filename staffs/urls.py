from django.urls import path

from . import views

urlpatterns = [
    path('', views.staffs, name='staffs'),
    path('create_staff/', views.create_staff, name='create_staff'),
    path('delete_staff/<int:id_staff>/', views.delete_staff, name='delete_staff'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('import_staff/', views.import_staff, name='import_staff'),
]
