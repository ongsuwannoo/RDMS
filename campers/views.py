from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from index.views import getPersonal, savePersonal, Personal
from personal.models import Personal
from .models import Camper
from .forms import *
from django.contrib import messages
# Create your views here.

def campers(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True
    return render(request, 'campers.html', context)
    
def camper_detail(request, id_camp, id_camper):
    context = {}
    context['id_camp'] = id_camp
    context['name'] = getPersonal(request)['name']
    if id_camp:
        context['active_camp'] = True
    return render(request, 'camper_detail.html', context)

def create_camper(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    camper_detail = Camper.objects.all()
    if id_camp:
        context['active_camp'] = True
    if request.method == 'POST':
        post = request.POST
        
        camp = Camp.objects.get(pk=id_camp)
        personal = savePersonal(request)

        form = CamperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # school = post.get('school')
        # parent_name = post.get('parent_name')
        # profile_pic = post.get('profile_pic')
        # group = post.get('group')
        # camper = Camper(
        #     camp = camp,
        #     personal = personal,
        #     group = group,
        # )
        # camper.save()
        print('successfully add to database')
        return HttpResponseRedirect('../../../../camp/%d/campers/'%id_camp)
    else:
        form = CamperForm()
        context['form'] = form
   
    return render(request, 'create_camper.html', context)
