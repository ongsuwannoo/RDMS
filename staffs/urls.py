from django.urls import path

from . import views

urlpatterns = [
    path('', views.staffs, name='staffs'),
    path('create_staff/', views.create_staff, name='create_staff'),
    path('import_staff/', views.import_staff, name='import_staff'),
]
