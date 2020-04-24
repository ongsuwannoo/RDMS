from django.shortcuts import render
from index.views import getPersonal
from .models import *
from django.shortcuts import redirect, render


# from .serializers import *

# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# Create your views here.

def camp(request, id_camp=""):
    context = {}
    context['id_camp'] = id_camp
    context['name'] = getPersonal(request)['name']
    
    sex = {'M':'Mr.', 'F':'Miss.'}
    if id_camp:
        camp = Camp.objects.get(pk=id_camp)
        camp.head.sex = sex[camp.head.sex]
        context['active_camp'] = True
        context['camp'] = camp
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
    context = {}
    context['id_camp'] = id_camp
    context['name'] = getPersonal(request)['name']
    if id_camp:
        context['active_camp'] = True

    if request.method == 'POST':
        pass
    
    return render(request, 'create_department_mc.html', context)

# @csrf_exempt
def create_department_mc_api(request):
    context = {}
    # context['id_camp'] = id_camp
    # context['name'] = getPersonal(request)['name']
    # if id_camp:
    #     context['active_camp'] = True

    # if request.method == 'POST':
    #     pass
    
    return render(request, 'create_department_mc.html', context)
