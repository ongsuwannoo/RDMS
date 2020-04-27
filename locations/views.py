from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *
from index.views import getPersonal

# Create your views here.
def locations(request, id_camp, id_location=""):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True

    context['id_location'] = id_location
    if id_location:
        location = Location.objects.get(pk=id_location)
        context['locations'] = location
        
    else:
        location = Location.objects.all()
        context['locations'] = location
    return render(request, 'locations.html', context)

def create_location (request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True
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
        # return redirect('locations')
        return HttpResponseRedirect('../../../%d/locations'%id_camp)
    return render(request, 'create_location.html', context)