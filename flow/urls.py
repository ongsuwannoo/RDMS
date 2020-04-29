from django.urls import path

from . import views

urlpatterns = [
    path('', views.flow, name='flow'),
    path('addFlow/', views.addFlow, name='addFlow'),
    # path('deleteFlow/<int:id_flow>', views.FlowView, name='deleteFlow'),
]
