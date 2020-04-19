from django.shortcuts import render
from index.views import getPersonal
# Create your views here.

def campers(request, number):
    context = {}
    context['number'] = number
    context['name'] = getPersonal(request)['name']
    if number:
        context['active_camp'] = True
    return render(request, 'campers.html', context)
    