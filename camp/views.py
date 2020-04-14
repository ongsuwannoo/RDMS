from django.shortcuts import render
# Create your views here.

def camp(request):
    context = {}
    return render(request, template_name ='camp.html', context=context)