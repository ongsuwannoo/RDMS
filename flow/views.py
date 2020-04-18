from django.shortcuts import render
from index.views import getPersonal

# Create your views here.

def flow(request):
    context = getPersonal(request)
    return render(request, 'flow.html', context)