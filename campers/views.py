from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from index.views import getPersonal
from personal.models import Personal
from .models import Camper
# Create your views here.

def campers(request, id_camp):
    context = {}
    context['id_camp'] = id_camp
    context['name'] = getPersonal(request)['name']
    if id_camp:
        context['active_camp'] = True
    return render(request, 'campers.html', context)
    
def camper_detail(request, id_camp, id_camper):
    context = {}
    context['id_camp'] = id_camp
    context['name'] = getPersonal(request)['name']
    if id_camp:
        context['active_camp'] = True
    print(id_camper)
    return render(request, 'camper_detail.html', context)

def create_camper(request, id_camp):
    context = {}
    context['id_camp'] = id_camp
    context['name'] = getPersonal(request)['name']
    camper_detail = Camper.objects.all()
    if id_camp:
        context['active_camp'] = True
        if request.method == 'POST':
            camper = Personal.objects.create(
                nick_name= request.POST.get('nick_name'),
                blood_type = request.POST.get('blood_type'),
                birthday = request.POST.get('birthday'),
                religion = request.POST.get('religion'),
                food_allergy = request.POST.get('food_allergy'),
                congenital_disease = request.POST.get('congenital_disease'),
                shirt_size = request.POST.get('shirt_size'),
            )
            print('successfully add to database')
        else:
            camper = Personal.objects.none()
    
    return render(request, 'create_camper.html', context)


# @csrf_exempt
# def api(request):
#     data = json.loads(request.body)
#     response = {
#         'input': data['tofind'],
#         'output': 'Your username is %s' % data['tofind']
#     }   
 
#     return JsonResponse(response, status=200)
