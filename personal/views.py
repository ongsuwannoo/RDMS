from django.shortcuts import render
from index.views import getPersonal

# Create your views here.

def profile(request):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True
    return render(request, 'profile.html', context)