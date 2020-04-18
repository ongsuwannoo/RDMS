from django.shortcuts import render
from index.views import getPersonal

# Create your views here.

def staffs(request):
    context = getPersonal(request)
    return render(request, 'staffs.html', context)