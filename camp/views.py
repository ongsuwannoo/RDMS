from django.shortcuts import render
from index.views import getPersonal, group_required
from .models import *
from staffs.models import Staff
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from .serializers import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.views import APIView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from campers.models import Camper
# Create your views here.


@login_required
def camp(request, id_camp=""):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    sex = {'M': 'Mr.', 'F': 'Miss.'}
    if id_camp:
        camp = Camp.objects.get(pk=id_camp)
        departments = reversed(Department.objects.filter(camp_id=id_camp))
        MCs = reversed(MC.objects.filter(camp_id=id_camp))
        count_total_staff = Staff.objects.select_related(
            'camp').filter(camp_id=id_camp).count
        count_total_camper = Camper.objects.select_related(
            'camp').filter(camp_id=id_camp).count

        camp.head.sex = sex[camp.head.personal.sex]
        context['active_camp'] = True
        context['camp'] = camp
        context['departments'] = departments
        context['MCs'] = MCs
        context['count_total_staff'] = count_total_staff
        context['count_total_camper'] = count_total_camper
        context['amount'] = camp.amount
        messages.info(request, 'ยินดีตอนรับสู่ค่าย '+camp.name)
    else:
        user = request.user
        staff = Staff.objects.filter(personal=user.personal)
        if staff:
            staff = staff[0]
            camp = Camp.objects.filter(pk=staff.camp.id)
        else:
            camp = Camp.objects.filter(head=user)
        context['camps'] = camp
        context['active_camp'] = False

    return render(request, 'camp.html', context)


@group_required('manager', login_url='/camp/')
def create_camp(request):
    context = getPersonal(request)
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        amount = request.POST.get('amount')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        logo = request.FILES.get('logo_pic')
        camp = Camp(
            head=user,
            name=name,
            desc=desc,
            amount=amount,
            start_date=start_date,
            end_date=end_date,
            logo=logo
        )
        camp.save()
        messages.success(request, 'ดำเนินการสร้าง '+name +
                         ' แล้ว ขอให้สนุกกับการจัดค่าย')
        return redirect('camp')
    return render(request, 'create_camp.html', context)


@group_required('manager', '/camp/')
def create_department_mc(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True

    if request.method == 'POST':
        camp = Camp.objects.get(pk=id_camp)
        choose = request.POST.get('choose')

        if choose == 'department':
            name = request.POST.get('name_department')
            typeOfDepartment = request.POST.get('typeOfDepartment')
            desc = request.POST.get('desc_department')

            department = Department(
                camp=camp,
                name=name,
                typeOfDepartment=typeOfDepartment,
                desc=desc
            )
            department.save()
            messages.success(request, 'ดำเนินการสร้างฝ่าย '+name+' แล้ว')

        elif choose == 'MC':
            name = request.POST.get('name_MC')
            typeOfMC = request.POST.get('typeOfMC')
            desc = request.POST.get('desc_MC')

            mc = MC(
                camp=camp,
                name=name,
                typeOfMC=typeOfMC,
                desc=desc
            )
            mc.save()
            messages.success(request, 'ดำเนินการสร้าง MC '+name+' แล้ว')

        return HttpResponseRedirect('../../../camp/%d/' % id_camp)
    return render(request, 'camp.html', context)


class DepartmentView(APIView):
    def get(self, request):
        id_department = request.query_params['id_department']
        department = Department.objects.get(pk=id_department)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data, status=status.HTTP_200_OK)
