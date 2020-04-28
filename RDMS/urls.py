"""RDMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from camp.views import DepartmentView
from locations.views import LocationView
from staffs.views import get_staffs_api
from flow.views import flow_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('camp/', include('camp.urls')),
    path('profile/', include('personal.urls')),
    path('api/getDepartment/', DepartmentView.as_view(), name='DepartmentView'),
    path('api/getLocation/', LocationView.as_view(), name='LocationView'),
    path('api/getStaffsDetail/<int:id_staff>', get_staffs_api, name='get_staffs_api'),
    path('api/flow_api/<int:id_camp>', flow_api, name='flow_api'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
