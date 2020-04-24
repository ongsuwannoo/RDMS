from django.shortcuts import render
from index.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from personal.models import *
from index.models import user
from camp.models import Camp

# Create your views here.

def register(request):
    context = {}
    context['nextStep'] = ['username', 'password1', 'password2', 'email']
    if request.method == 'POST':
        form = regForm(request.POST, request.FILES)
        context['form'] = form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.personal_id = savePersonal(request)
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = regForm()
        context['form'] = form
    return render(request, 'register.html', context)

def my_login(request):
    logout(request)
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.POST.get('next')
            if next_url and next_url != '/login/':
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context = {
                'username': username,
                'error': 'Wrong username or password'
            }

    return render(request, 'login.html', context)

@login_required
def my_logout(request):
    logout(request)
    return redirect('index')

def savePersonal(request):
    context = {}
    nick_name = request.POST.get('nick_name')
    blood_type = request.POST.get('blood_type')
    birthday = request.POST.get('birthday')
    religion = request.POST.get('religion')
    food_allergy = request.POST.get('food_allergy')
    congenital_disease = request.POST.get('congenital_disease')
    shirt_size = request.POST.get('shirt_size')

    personal = Personal(
        nick_name = nick_name,
        blood_type = blood_type,
        birthday = birthday,
        religion = religion,
        food_allergy = food_allergy,
        congenital_disease = congenital_disease,
        shirt_size = shirt_size
    )
    personal.save()
    return personal

def index(request):
    context = {}
    camp = Camp.objects.all()
    context['camps'] = reversed(camp)
    return render(request, 'index.html', context)

def getPersonal(request):

    if request.user.is_authenticated:
        user = request.user
        sex = {'M':'Mr.', 'F':'Miss.'}
        name = sex[user.sex] + user.first_name + ' ' + user.last_name
        profile_pic = user.profile_pic
        context = {
            'name': name,
            'profile_pic': profile_pic
        }
        return context
