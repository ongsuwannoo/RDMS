from django.shortcuts import render, redirect
from index.views import getPersonal, savePersonal, Personal
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

from .serializers import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def staffs(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    context['staffs'] = Staff.objects.select_related('personal')

    if id_camp:
        context['active_camp'] = True
    return render(request, 'staffs.html', context)

def create_staff(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True

    if request.method == 'POST':
        post = request.POST
        camp = Camp.objects.get(pk=id_camp)
        personal = savePersonal(request)

        position = post.get('position')
        group = post.get('group')

        staff = Staff(
            camp = camp,
            personal = personal,
            position = position,
            group = group,
        )
        staff.save()
        return HttpResponseRedirect('../../../../camp/%d/staffs/'%id_camp)
    else:
        form = StaffForm()
        context['form'] = form
    return render(request, 'create_staff.html', context)

@csrf_exempt
@api_view(['GET', 'POST'])
def get_staffs_api(request, id_staff):
    context = {}
    if request.method == 'GET':
        staffs = Staff.objects.get(pk=id_staff)
        serializer = StaffSerializer(staffs)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return render(request, 'staffs.html', context)
