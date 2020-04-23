from django.http import HttpResponse
from django.shortcuts import render

from index.views import getPersonal

# Create your views here.

def campers(request, id_camp):
    context = {}
    context['id_camp'] = id_camp
    context['name'] = getPersonal(request)['name']
    if id_camp:
        context['active_camp'] = True
    return render(request, 'campers.html', context)
    
def camper_detail(request, number):
    context = {}
    return render(request, 'camper_detail.html', context)
