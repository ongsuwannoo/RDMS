from django.shortcuts import render
from index.views import getPersonal

# Create your views here.

def profile(request):
    context = getPersonal(request)
    return render(request, 'profile.html', context)