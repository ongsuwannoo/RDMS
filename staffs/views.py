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

import csv, io
from django.contrib import messages

# Create your views here.

def staffs(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    context['staffs'] = reversed(Staff.objects.select_related('personal'))

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

        if post.get('department') != '0':
            department = Department.objects.get(pk=post.get('department'))
            staff.department = department
        
        staff.save()
        return HttpResponseRedirect('../../../../camp/%d/staffs/'%id_camp)
    else:
        form = StaffForm()
        context['form'] = form
        context['departments'] = Department.objects.filter(camp_id=id_camp)
    return render(request, 'create_staff.html', context)


def import_staff(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True
    template = "import_staff.html"

    data = Staff.objects.all()
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, context)

    csv_file = request.FILES['file']
    

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
        
    data_set = csv_file.read().decode('utf-8-sig')
    dic = csv.DictReader(io.StringIO(data_set), delimiter=",")
    
    camp = Camp.objects.get(pk=id_camp)
    for i in dic:
        # i.update((k, [v]) for k, v in i.items())
        
        personal = savePersonal(i)

        department = Department.objects.filter(name=i['department'], camp_id=id_camp)

        position = 'staff'
        group = '-'

        staff = Staff(
            camp = camp,
            personal = personal,
            position = position,
            group = group,
        )

        if department:
            staff.department = department

        staff.save()
    return HttpResponseRedirect('../../../../camp/%d/staffs/'%id_camp)

def test(request):
    print(request['sid'])

@csrf_exempt
@api_view(['GET', 'POST'])
def get_staffs_api(request, id_staff):
    context = {}
    if request.method == 'GET':
        staffs = Staff.objects.get(pk=id_staff)
        serializer = StaffSerializer(staffs)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return render(request, 'staffs.html', context)
