from django.shortcuts import render
from index.views import getPersonal
# Create your views here.

def campers(request):
    context = getPersonal(request)
    return render(request, 'campers.html', context)
    