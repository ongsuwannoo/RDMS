from django.shortcuts import render
from index.views import getPersonal

# Create your views here.

def flow(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True
    
    if request.method == 'POST':
        print('OK')
    return render(request, 'flow.html', context)