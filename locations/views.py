from django.shortcuts import render
from index.views import getPersonal

# Create your views here.

def locations(request):
    context = getPersonal(request)
    return render(request, 'locations.html', context)