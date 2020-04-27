from django.shortcuts import render
from index.views import getPersonal
from locations.models import Location
from .models import Flow
from camp.models import Department, MC, Camp
import datetime

from .serializers import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def flow(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True

    if request.method == 'POST':
        post = request.POST
        time = post.get('time').split(' - ')
        t1 = int((time[0]).split(':')[0])
        t2 = int((time[0]).split(':')[1])
        time_start = datetime.time(t1, t2)
        t1 = int((time[1]).split(':')[0])
        t2 = int((time[1]).split(':')[1])
        time_end = datetime.time(t1, t2)

        activity = post.get('activity')
        sub_time = post.get('sub_time')
        desc = post.get('desc')
        department = post.get('department')
        mc = post.get('department')
        location = post.get('location')
        note = post.get('note')

        department = Department.objects.get(pk=department)
        # mc = MC.objects.get(pk=mc)
        location = Location.objects.get(pk=location)
        camp = Camp.objects.get(pk=id_camp)

        flow = Flow(
            time_start = time_start,
            time_end = time_end,
            activity = activity,
            sub_time = sub_time,
            desc = desc,
            department = department,
            # mc = mc,
            location = location,
            camp = camp,
            note = note
        )
        flow.save()
    else:
        context['location'] = Location.objects.all()
        context['department'] = Department.objects.filter(camp_id=id_camp)
        context['mc'] = MC.objects.filter(camp_id=id_camp)

    return render(request, 'flow.html', context)

@csrf_exempt
@api_view(['GET'])
def flow_api(request, id_camp):
    if request.method == 'GET':
        flow = Flow.objects.filter(camp_id=id_camp)
        serializer = FlowSerializer(flow, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# @csrf_exempt
# @api_view(['POST'])
def addFlow(request):
    if request.method == 'POST':
        serializer = FlowSerializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        