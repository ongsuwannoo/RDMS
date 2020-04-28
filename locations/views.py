from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *
from index.views import getPersonal, group_required
from .serializers import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.views import APIView

# Create your views here.
def locations(request, id_camp, id_location=""):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True

    context['id_location'] = id_location
    if id_location:
        location = Location.objects.get(pk=id_location)
        context['locations'] = location
        
    else:
        location = Location.objects.all()
        context['locations'] = location
    return render(request, 'locations.html', context)

@group_required('manager', 'head', 'mc')
def create_location (request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True
    if request.method == 'POST':
        # user = request.user
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        # start_date = request.POST.get('start_date')
        # end_date = request.POST.get('end_date')
        logo = request.FILES.get('logo')
        location = Location(
            # head = user,
            name = name,
            desc = desc,
            # start_date = start_date,
            # end_date = end_date,
            logo = logo
        )
        location.save()
        # return redirect('locations')
        messages.success(request, 'สร้างสถานที่ '+name+' แล้ว')
        return HttpResponseRedirect('../../../%d/locations'%id_camp)
    return render(request, 'create_location.html', context)

@group_required('manager', 'head', 'mc')
def update_location(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp

    if request.method == 'POST':
        post = request.POST
        post_file = request.FILES
        location = Location.objects.get(pk=post.get('id'))
        location.name = post.get('name')
        location.desc = post.get('desc')
        # location.logo = post_file.get('logo')
        location.save()
        messages.success(request, 'แก้ไขสถานที่ '+post.get('name')+' เรียบร้อย')
    return HttpResponseRedirect('../../../%d/locations'%id_camp)

@group_required('manager', 'head', 'mc')
def delete_location(request, id_camp, id_location=""):
    context = getPersonal(request)
    context['id_camp'] = id_camp

    location = Location.objects.get(pk=id_location)
    location.delete()
    messages.warning(request, 'ลบสถานที่ '+location.name+' เรียบร้อย')
    return HttpResponseRedirect('../../../../%d/locations' % id_camp)
    # return redirect(to='locations')

class LocationView(APIView):
    def get(self, request):
        id_location = request.query_params['id_location']
        location = Location.objects.get(pk=id_location)
        serializer = LocationSerializer(location)
        return Response(serializer.data, status=status.HTTP_200_OK)

