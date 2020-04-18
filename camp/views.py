from django.shortcuts import render
from index.views import getPersonal
from .models import *
from django.shortcuts import redirect, render
# Create your views here.

def camp(request, camp=""):
    user = request.user
    camp = Camp.objects.filter(head=user)
    # head = user.objects.get(pk=camp.head)
    context = {
        'name': getPersonal(request)['name'],
        'camps': camp,
    }
    print(context)
    return render(request, 'camp.html', context)

def create_camp(request):
    context = getPersonal(request)
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        logo = request.FILES.get('logo')
        camp = Camp(
            head = user,
            name = name,
            desc = desc,
            start_date = start_date,
            end_date = end_date,
            logo = logo
        )
        camp.save()
        return redirect('camp')
    return render(request, 'create_camp.html', context)
