from django.shortcuts import render
from index.views import getPersonal
from .models import *
from django.shortcuts import redirect, render
# Create your views here.

def camp(request, number=""):
    context = {}
    context['number'] = number
    context['name'] = getPersonal(request)['name']
    if number:
        camp = Camp.objects.get(pk=number)
        context['active_camp'] = True
        context['camp'] = camp
    else:
        user = request.user
        camp = Camp.objects.filter(head=user)
        context['camps'] = camp
        context['active_camp'] = False
        
    return render(request, 'camp.html', context)

def campers(request, number):
    context = {}
    return render(request, 'camp.html', context)

def create_camp(request):
    context = getPersonal(request)
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        logo = request.FILES.get('logo')
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
