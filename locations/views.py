from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from index.views import getPersonal

# Create your views here.

def locations(request,id_location=""):
    context = {}
    context['id_location'] = id_location
    if id_location:
        location = Location.objects.get(pk=id_location)
        context['locations'] = location
        # context['active_camp'] = True
    else:
        location = Location.objects.all()
        context['locations'] = location
    return render(request, 'locations.html', context)

def create_location (request):
    context = getPersonal(request)
    if request.method == 'POST':
        # user = request.user
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        # start_date = request.POST.get('start_date')
        # end_date = request.POST.get('end_date')
        logo = request.FILES.get('logo')
        location = Location(
            # head = user,
            name = name,
            desc = desc,
            # start_date = start_date,
            # end_date = end_date,
            logo = logo
        )
        location.save()
        return redirect('locations')
    return render(request, 'create_location.html', context)