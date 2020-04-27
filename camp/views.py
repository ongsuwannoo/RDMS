from django.shortcuts import render
from index.views import getPersonal
from .models import *
from staffs.models import Staff
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect


from .serializers import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def camp(request, id_camp=""):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    sex = {'M':'Mr.', 'F':'Miss.'}
    if id_camp:
        camp = Camp.objects.get(pk=id_camp)
        departments = reversed(Department.objects.filter(camp_id=id_camp))
        MCs = reversed(MC.objects.filter(camp_id=id_camp))
        count_total_staff = Staff.objects.select_related('camp').filter(camp_id=id_camp).count

        camp.head.sex = sex[camp.head.personal.sex]
        context['active_camp'] = True
        context['camp'] = camp
        context['departments'] = departments
        print(context['departments'])
        context['MCs'] = MCs
        context['count_total_staff'] = count_total_staff
    else:
        user = request.user
        camp = Camp.objects.filter(head=user)
        context['camps'] = camp
        context['active_camp'] = False
        
    return render(request, 'camp.html', context)

def create_camp(request):
    context = getPersonal(request)
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        logo = request.FILES.get('logo_pic')
        camp = Camp(
            head = user,
            name = name,
            desc = desc,
            start_date = start_date,
            end_date = end_date,
            logo = logo
        )
        camp.save()
        return redirect('camp')
    return render(request, 'create_camp.html', context)

def create_department_mc(request, id_camp):
    print('create_department_mc')
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True

    if request.method == 'POST':
        camp = Camp.objects.get(pk=id_camp)
        choose =  request.POST.get('choose')
        
        if choose == 'department':
            name = request.POST.get('name_department')
            typeOfDepartment = request.POST.get('typeOfDepartment')
            desc = request.POST.get('desc_department')

            department = Department(
                camp = camp,
                name = name,
                typeOfDepartment = typeOfDepartment,
                desc = desc
            )
            department.save()

        elif choose == 'MC':
            name = request.POST.get('name_MC')
            typeOfMC = request.POST.get('typeOfMC')
            desc = request.POST.get('desc_MC')

            mc = MC(
                camp = camp,
                name = name,
                typeOfMC = typeOfMC,
                desc = desc
            )
            mc.save()

        return HttpResponseRedirect('../../../camp/%d/'%id_camp)
    return render(request, 'camp.html', context)

@csrf_exempt
@api_view(['GET', 'POST'])
def get_department_api(request, id_department):
    context = {}
    if request.method == 'GET':
        department = Department.objects.get(pk=id_department)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return render(request, 'create_department_mc.html', context)
