from django.shortcuts import render, redirect
from index.views import getPersonal, savePersonal, Personal, group_required
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

from .serializers import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group
from index.models import user
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics

import csv
import io
from django.contrib import messages
from personal.views import *

# Create your views here.


def staffs(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    context['staffs'] = reversed(Staff.objects.select_related(
        'personal').filter(camp_id=id_camp))

    if id_camp:
        context['active_camp'] = True
    return render(request, 'staffs.html', context)


@group_required('manager', 'head')
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
            camp=camp,
            personal=personal,
            position=position,
            group=group,
        )

        if post.get('department') != '0':
            department = Department.objects.get(pk=post.get('department'))
            staff.department = department

        staff.save()
        messages.success(request, 'เพิ่ม Staff '+personal.first_name+' แล้ว')
        return HttpResponseRedirect('../../../../camp/%d/staffs/' % id_camp)
    else:
        form = StaffForm()
        context['form'] = form
        context['departments'] = Department.objects.filter(camp_id=id_camp)
    return render(request, 'create_staff.html', context)


@group_required('manager', 'head')
def add_staff(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True

    if request.method == 'POST':
        post = request.POST

        camp = Camp.objects.get(pk=id_camp)

        username = post.get('username')
        data_user = user.objects.get(username=username)
        personal = Personal.objects.get(pk=data_user.personal_id)

        position = post.get('position')
        group = post.get('group')

        staff = Staff(
            camp=camp,
            personal=personal,
            position=position,
            group=group,
        )

        if post.get('department') != '0':
            department = Department.objects.get(name=post.get('department'))
            staff.department = department

        if post.get('mc') != '0':
            mc = MC.objects.get(name=post.get('mc'))
            staff.mc = mc

        my_group = Group.objects.get(name='staff') 
        my_group.user_set.add(data_user)

        staff.save()
        messages.success(request, 'เพิ่ม Staff '+personal.first_name+' แล้ว')
        return HttpResponseRedirect('../../../../camp/%d/staffs/' % id_camp)

    else:
        form = StaffForm()
        context['camp'] = Camp.objects.get(pk=id_camp)
        context['userAll'] = user.objects.all()
        context['form'] = form
        context['MCs'] = MC.objects.filter(camp_id=id_camp)
        context['departments'] = Department.objects.filter(camp_id=id_camp)
    return render(request, 'add_staff.html', context)


@group_required('manager', 'head')
def delete_staff(request, id_camp, id_staff=""):
    context = getPersonal(request)
    context['id_camp'] = id_camp

    staff = Staff.objects.get(pk=id_staff)
    personal = Personal.objects.get(pk=staff.personal.id)
    personal.delete()
    staff.delete()
    messages.warning(request, 'ลบ '+staff.personal.first_name +
                     ' '+staff.personal.last_name+' เรียบร้อย')
    return HttpResponseRedirect('../../../../%d/staffs' % id_camp)


def import_staff(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True
    template = "import_staff.html"

    data = Staff.objects.all()
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        count = 0
        camp = Camp.objects.get(pk=id_camp)
        # for _ in range(200):
        #     per = randomPersonal()
        #     per['sid'] = '61070'+('%03d'%random.randrange(1, 500))
        #     personal = savePersonal(per)
        #     rand = randomStaff()

        #     department = Department.objects.filter(name=rand['department'], camp_id=id_camp)
        #     mc = MC.objects.filter(name=rand['mc'], camp_id=id_camp)

        #     group = '-'
        #     staff = Staff(
        #         camp = camp,
        #         personal = personal,
        #         position = rand['position'],
        #     )
        #     check = 0

        #     if department:
        #         staff.department = department[0]
        #     else:
        #         name = rand['department']
        #         typeOfDepartment = '-'
        #         desc = '-'

        #         if name in ['ค่าย IOT', 'ค่าย Network','ค่าย App',' ค่าย Data','ค่าย Game']:
        #             depart = Department.objects.filter(typeOfDepartment=name, camp_id=id_camp)

        #             if not depart:
        #                 typeOfDepartment = 'วิชาการ'
        #                 group = 'วิชาการ'
        #             else:
        #                 check = 1

        #         if name == 'พี่บ้าน':
        #             depart = Department.objects.filter(typeOfDepartment=name, camp_id=id_camp)

        #             if not depart:
        #                 typeOfDepartment = 'ส้นทนาการ'
        #                 group = 'ส้นทนาการ'
        #             else:
        #                 check = 1

        #         if check == 0:
        #             department = Department(
        #                 camp = camp,
        #                 name = name,
        #                 typeOfDepartment = typeOfDepartment,
        #                 desc = desc
        #             )

        #             department.save()
        #             staff.department = department

        #     if mc:
        #         staff.mc = mc[0]
        #     else:
        #         name = rand['mc']
        #         if rand['mc'] != '-' and check == 0:
        #             typeOfMC = '-'
        #             desc = '-'

        #             mc = MC(
        #                 camp = camp,
        #                 name = name,
        #                 typeOfMC = typeOfMC,
        #                 desc = desc
        #             )

        #             mc.save()
        #             staff.mc = mc

        #     staff.group = group

        #     staff.save()

        #     count += 1
        #     print('save staff', count)
        return render(request, template, context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('utf-8-sig')
    dic = csv.DictReader(io.StringIO(data_set), delimiter=",")

    camp = Camp.objects.get(pk=id_camp)
    # นับจำนวน staff ทั้งหมด
    count = 0
    for i in dic:
        # i.update((k, [v]) for k, v in i.items())

        personal = savePersonal(i)

        department = Department.objects.filter(
            name=i['department'], camp_id=id_camp)

        position = 'staff'
        group = '-'

        staff = Staff(
            camp=camp,
            personal=personal,
            position=position,
            group=group,
        )

        if department:
            staff.department = department[0]

        staff.save()
        count += 1
    messages.warning(request, 'ทำการ import staff จำนวน ' +
                     str(count)+' คน หากผิดพลาดโปรดติดต่อผู้ดูแล')
    return HttpResponseRedirect('../../../../camp/%d/staffs/' % id_camp)


@csrf_exempt
@api_view(['GET'])
def get_staffs_api(request, id_staff):
    """
    API ดึงข้อมูล staff โดย id_staff
    """
    context = {}
    if request.method == 'GET':
        staffs = Staff.objects.get(pk=id_staff)
        serializer = StaffSerializer(staffs)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return render(request, 'staffs.html', context)


class StaffsView(generics.ListAPIView):
    serializer_class = StaffSerializer

    def get_queryset(self):
        id_camp = self.request.query_params['id_camp']
        search = self.request.query_params['search']
        filter_staff = Staff.objects.select_related('personal').filter(
            camp_id=id_camp,
            personal__first_name__startswith=search)
        return filter_staff
