from django.shortcuts import render
from index.views import getPersonal

# Create your views here.

def flow(request, id_camp):
    context = {}
    context['id_camp'] = id_camp
    context['name'] = getPersonal(request)['name']
    if id_camp:
        context['active_camp'] = True
    return render(request, 'flow.html', context)