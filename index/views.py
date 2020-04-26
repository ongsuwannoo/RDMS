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
    post_data = request

    # แปลงจาก queryset เป็น dict
    if type(post_data) != dict:
        print('type data != dict')
        post_data = dict(request.POST)
        post_data.update(request.FILES)
    
    # เช็คว่า value เป็น List ไหม แล้วแปลงเป็น String
    for i in post_data:
        if type(post_data[i]) == list:
            post_data[i] = post_data[i][0]

    sid = post_data.get('sid')

    first_name = post_data.get('first_name')
    last_name = post_data.get('last_name')
    nick_name = post_data.get('nick_name')
    
    sex = post_data.get('sex')
    phone = post_data.get('phone')
    email = post_data.get('email')

    blood_type = post_data.get('blood_type')
    birthday = post_data.get('birthday')
    religion = post_data.get('religion')
    food_allergy = post_data.get('food_allergy')
    congenital_disease = post_data.get('congenital_disease')
    shirt_size = post_data.get('shirt_size')
    
    profile_pic = post_data.get('profile_pic')

    personal = Personal(
        sid = sid,

        first_name = first_name,
        last_name = last_name,
        nick_name = nick_name,
        
        sex = sex,
        phone = phone,
        email = email,

        blood_type = blood_type,
        birthday = birthday,
        religion = religion,
        food_allergy = food_allergy,
        congenital_disease = congenital_disease,
        shirt_size = shirt_size,
        
        profile_pic = profile_pic
    )
    print('save personal success!')
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
        context = {}
        personal = Personal.objects.get(pk=user.id)
        sex = {'M':'Mr.', 'F':'Miss.'}
        name = sex[personal.sex] + personal.first_name + ' ' + personal.last_name
        context['name'] = name
        context['personal'] = personal
        
        return context
