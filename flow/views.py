from django.shortcuts import render
from index.views import getPersonal, group_required
from locations.models import Location
from .models import Flow
from camp.models import Department, MC, Camp
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .serializers import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from personal.views import get_flow
import random
# Create your views here.

def flow(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True
    context['locations'] = Location.objects.all()
    context['departments'] = Department.objects.filter(camp_id=id_camp)
    context['mc'] = MC.objects.filter(camp_id=id_camp)

    return render(request, 'flow.html', context)

@group_required('manager')
def addFlow(request, id_camp, id_flow=""):
    if request.method == 'POST':
        post = request.POST
        t1 = int((post.get('time_start')).split(':')[0])
        t2 = int((post.get('time_start')).split(':')[1])
        time_start = datetime.time(t1, t2)
        t1 = int((post.get('time_end')).split(':')[0])
        t2 = int((post.get('time_end')).split(':')[1])
        time_end = datetime.time(t1, t2)
        activity = post.get('activity')
        sub_time = post.get('sub_time')
        desc = post.get('desc')
        department = post.get('department')
        mc = post.get('department')
        location = post.get('location')
        note = post.get('note')
        
        department = Department.objects.filter(pk=department)
        mc = MC.objects.filter(pk=mc)
        location = Location.objects.filter(pk=location)
        camp = Camp.objects.get(pk=id_camp)

        id_flow = post.get('id_flow')

        if not id_flow:
            flow = Flow(
                time_start = time_start,
                time_end = time_end,
                activity = activity,
                sub_time = sub_time,
                desc = desc,
                camp = camp,
                note = note
            )
            messages.success(request, 'เพิ่ม Flow '+activity+' แล้ว')

        else:
            flow = Flow.objects.get(pk=id_flow)
            flow.time_start = time_start
            flow.time_end = time_end
            flow.activity = activity
            flow.sub_time = sub_time
            flow.desc = desc
            flow.camp = camp
            flow.note = note
            messages.success(request, 'แก้ไข Flow '+activity+' แล้ว')

        if location:
            flow.location = location[0]

        if department:
            flow.department = department[0]

        elif mc:
            flow.mc = mc[0]

        flow.save()
        return HttpResponseRedirect('../../../../camp/%d/flow'%id_camp)


@api_view(['GET'])
def flow_api(request, id_camp):
    """
    API FLOW
    id_camp = ค่าคงที่ของ camp ระบุ camp
    method GET = ดึงค่าตารางไปเปิดในหน้า flow.html โดยใช้ id_camp
    """

    # for i in range(113):

    #     gen_flow = get_flow(i)
    #     department = Department.objects.filter(name=gen_flow['department'])
    #     mc = MC.objects.filter(name=gen_flow['department'])
    #     location = Location.objects.filter(name=gen_flow['location'])
    #     camp = Camp.objects.get(pk=id_camp)

    #     # if not id_flow:
    #     #     flow = Flow(
    #     #         time_start = time_start,
    #     #         time_end = time_end,
    #     #         activity = activity,
    #     #         sub_time = sub_time,
    #     #         desc = desc,
    #     #         camp = camp,
    #     #         note = note
    #     #     )
        
    #     flow = Flow(
    #         time_start = gen_flow['time_start'],
    #         time_end = gen_flow['time_end'],
    #         activity = gen_flow['activity'],
    #         sub_time = gen_flow['sub_time'],
    #         desc = gen_flow['desc'],
    #         camp = camp,
    #         note = gen_flow['note']
    #     )

    #     check = 0

    #     if gen_flow['department'][0] == 'M':
    #         if mc:
    #             flow.mc = mc[0]
    #         else:
    #             name = gen_flow['department']
    #             if gen_flow['department'] != '-' and check == 0:
    #                 typeOfMC = '-'
    #                 desc = '-'

    #                 mc = MC(
    #                     camp = camp,
    #                     name = name,
    #                     typeOfMC = typeOfMC,
    #                     desc = desc
    #                 )
    #                 print('MC save! '+name)
    #                 mc.save()
    #                 flow.mc = mc

    #     elif department:
    #         flow.department = department[0]
    #     else:
    #         name = gen_flow['department']
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
    #             print('department save! '+name)
    #             department.save()
    #             flow.department = department

    #     if location:
    #         flow.location = location[0]
    #     else:
    #         name = gen_flow['location']
    #         if gen_flow['location'] != '-' and check == 0:
    #             typeOfMC = '-'
    #             desc = '-'

    #             location = Location(
    #                 name = gen_flow['location'],
    #                 desc = "-",
    #                 logo = "logo/"+str(random.randrange(99999999))+random.choice(['.png', '.jpg'])
    #             )
    #             print('location save! '+name)
    #             location.save()
    #             flow.location = location
    #     print('flow save!', (i+1))
    #     flow.save()
        # break

    # id_flow = post.get('id_flow')

    if request.method == 'GET':
        flow = Flow.objects.filter(camp_id=id_camp)
        serializer = FlowSerializer(flow, many=True)
        messages.success(request, 'โหลดสำเร็จ')
        return Response(serializer.data, status=status.HTTP_200_OK)

@group_required('manager')
@api_view(['GET'])
def flow_api_delete(request, id_flow):
    """
    API FLOW
    id_camp = ค่าคงที่ของ camp ระบุ camp
    method GET = ดึงค่าตารางไปเปิดในหน้า flow.html โดยใช้ id_camp
    """
    if request.method == 'GET':
        flow = Flow.objects.get(pk=id_flow)
        flow.delete()
        messages.warning(request, 'ลบ Flow เรียบร้อย')
        return Response(status=status.HTTP_200_OK)

