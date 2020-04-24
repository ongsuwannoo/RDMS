from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from index.views import getPersonal

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
    if id_camp:
        context['active_camp'] = True
    return render(request, 'create_camper.html', context)

# @csrf_exempt
# def api(request):
#     data = json.loads(request.body)
#     response = {
#         'input': data['tofind'],
#         'output': 'Your username is %s' % data['tofind']
#     }   
 
#     return JsonResponse(response, status=200)
