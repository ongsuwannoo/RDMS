from django.shortcuts import render
from index.forms import *
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import request
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from personal.models import *
from index.models import user
from camp.models import Camp
from datetime import datetime
from django.contrib import messages

# Create your views here.

from six import text_type
from django.core.exceptions import PermissionDenied
from django.contrib.auth import REDIRECT_FIELD_NAME
from functools import wraps
from urllib.parse import urlparse
from django.shortcuts import resolve_url

def group_required(group, login_url=None, raise_exception=False):
    """
    Decorator for views that checks whether a user has a group permission,
    redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
    """
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group, )
        else:
            groups = group
        # First check if the user has the permission (even anon users)

        if user.groups.filter(name__in=groups).exists():
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False
    return my_user_passes_test(check_perms, login_url=login_url)

def my_user_passes_test(test_func, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the "HTTP_REFERER" page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            messages.error(request, 'สิทธิของคุณไม่สามารถทำได้ กรุณาติดต่อ Admin หรือ เปลี่ยนเป็น user อื่น')
            return redirect(request.META.get('HTTP_REFERER'))
        return _wrapped_view
    return decorator

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
            messages.success(
                request, 'สมัครสมาชิกสำเร็จแล้วยินดีต้อนรับ '+username+' สู่ RDMS')
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
                messages.info(
                    request, 'เข้าสู่ระบบสำเร็จแล้วยินดีต้อนรับ '+username+' สู่ RDMS')
                return redirect('index')
        else:
            context = {
                'username': username,
                'error': 'Wrong username or password'
            }

    return render(request, 'login.html', context)


def my_logout(request):
    logout(request)
    return redirect('index')


@login_required
def ChangePassword(request):
    context = {}
    if request.method == 'POST':
        username = request.user.username
        password = request.POST.get('password')
        re_password = request.POST.get('password_confirm')

        if password != re_password:
            messages.warning(request, 'Please correct the error below.')
        else:
            u = user.objects.get(username=username)
            u.set_password(password)
            u.save()
            messages.success(
                request, 'Your password was updated successfully!')
            return redirect('logout')

    return render(request, 'profile.html', context=context)


def index(request):
    context = {}
    if not request.user.is_authenticated:
        pass
    elif request.user.id and request.user.personal_id:
        context = getPersonal(request)
    else:
        if not request.user.personal_id:
            messages.warning(
                request, 'user ของคุณไม่มีการกรอกข้อมูล personal ระวังบัค')
    camp = Camp.objects.all()
    context['camps'] = reversed(camp)

    return render(request, 'index.html', context)


@login_required
def my_profile(request):
    context = getPersonal(request)
    if request.method == 'POST':
        post = request.POST
        user_personal_id = request.user.personal_id
        personal = updatePersonal(post, user_personal_id)
        context['personal'] = personal
        messages.success(request, 'อัพเดตโปรไฟล์เสร็จสมบูรณ์')
    return render(request, 'profile.html', context)


def getPersonal(request):

    if request.user.is_authenticated and request.user.personal_id:
        user = request.user
        context = {}
        personal = Personal.objects.get(pk=user.personal_id)
        sex = {'M': 'Mr.', 'F': 'Miss.'}
        name = sex[personal.sex] + \
            personal.first_name + ' ' + personal.last_name
        context['name'] = name
        context['personal'] = personal

        return context
    else:
        messages.warning(
            request, 'user ของคุณไม่มีการกรอกข้อมูล personal ระวังบัค')
        return {}


def savePersonal(request):
    """
    savePersonal() รับค่าได้ 2 ชนิด queryset และ dict
    เพราะว่าเวลา import ส่งเป็น dict จะสะดวกกว่า
    """
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
        sid=sid,

        first_name=first_name,
        last_name=last_name,
        nick_name=nick_name,

        sex=sex,
        phone=phone,
        email=email,

        blood_type=blood_type,
        birthday=birthday,
        religion=religion,
        food_allergy=food_allergy,
        congenital_disease=congenital_disease,
        shirt_size=shirt_size,

        profile_pic=profile_pic
    )
    personal.save()
    print('save personal success!')
    return personal


def updatePersonal(request, id):
    """
    รับ id personal มาด้วยเพื่อทำการอัพเดตค่าใน personal นั้น
    """
    print(request)

    context = {}
    post_data = request

    personal = Personal.objects.get(pk=id)
    birthday = post_data.get('birthday')

    # บัคเวลาส่งวันเกิดมา และแปลงให้เป็น type date เพราะเวลาส่งมาจะเป็น text
    # (ไม่ได้เปลี่ยนแปลงค่า แต่ค่าที่ html ส่งมามันเป็น text)
    # print(datetime.strptime(post.get('birthday'), '%Y-%m-%d').date() , '==', personal.birthday)
    if not datetime.strptime(birthday, '%Y-%m-%d').date() == personal.birthday or birthday == '':
        # ในกรณีที่ไม่ได้เปลี่ยนแปลงค่าวันเกิด ก็เท่ากับวันเกิดเดิม
        birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
    else:  # เปลี่ยนแปลงค่าวันเกิด ค่าที่ไปกดแก้ไขจะเป็น date เพราะดักไว้ที่ html แล้ว
        birthday = birthday

    sid = post_data.get('sid')
    first_name = post_data.get('first_name')
    last_name = post_data.get('last_name')
    nick_name = post_data.get('nick_name')
    # sex = post_data.get('sex')
    phone = post_data.get('phone')
    email = post_data.get('email')
    blood_type = post_data.get('blood_type')

    religion = post_data.get('religion')
    food_allergy = post_data.get('food_allergy')
    congenital_disease = post_data.get('congenital_disease')
    shirt_size = post_data.get('shirt_size')
    # profile_pic = post_data.get('profile_pic')

    personal.sid = sid
    personal.first_name = first_name
    personal.last_name = last_name
    personal.nick_name = nick_name
    # personal.sex = sex
    personal.phone = phone
    personal.email = email
    personal.blood_type = blood_type
    personal.birthday = birthday
    personal.religion = religion
    personal.food_allergy = food_allergy
    personal.congenital_disease = congenital_disease
    personal.shirt_size = shirt_size
    # personal.profile_pic = profile_pic
    personal.save()
    print('update personal success!')
    return personal
