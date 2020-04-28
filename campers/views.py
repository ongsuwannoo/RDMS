from datetime import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from index.views import Personal, getPersonal, savePersonal
from personal.models import Personal

from .forms import *
from .models import Camper

# Create your views here.

def campers(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    context['campers'] = reversed(Camper.objects.select_related('personal').filter(camp_id=id_camp))
    if id_camp:
        context['active_camp'] = True
    return render(request, 'campers.html', context)
    
def camper_detail(request, id_camp, id_camper):
    context = {}
    context['id_camp'] = id_camp
    context['id_camper'] = id_camper
    context['name'] = getPersonal(request)['name']
    context['camper'] = Camper.objects.filter(id=id_camper)
    
    #use to link to personal
    link = Camper.objects.values('personal_id')

    #get object with personal_id = link
    for camper_object in link:
        camper_id = camper_object['personal_id']

    #get date from camper_id = personal_id   
    get_date = Personal.objects.filter(id=camper_id).values('birthday')
    for date_object in get_date:
        #return as time.delta then convert them
        time_count_year = datetime.now().date() - date_object['birthday']
    
    #send year that already count as context
    context['birthday'] = time_count_year.days // 365
    if id_camp:
        context['active_camp'] = True
    return render(request, 'camper_detail.html', context)

def create_camper(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    # camper_detail = Camper.objects.all()
    if id_camp:
        context['active_camp'] = True

    if request.method == 'POST':
        post = request.POST
        
        camp = Camp.objects.get(pk=id_camp)

        personal = savePersonal(request)

        school = post.get('school')
        parent_phone = post.get('parent_phone')
        parent_name = post.get('parent_name')
        group = post.get('group')
        camper = Camper(
            camp = camp,
            personal = personal,
            school = school,
            parent_phone = parent_phone,
            parent_name = parent_name,
            group = group,
        )
        camper.save()
        messages.success(request, 'เพิ่ม Camper เรียบร้อยแล้ว')
        print('successfully add to database')
        return HttpResponseRedirect('../../../../camp/%d/campers/'%id_camp)
    else:
        form = CamperForm()
        context['form'] = form
   
    return render(request, 'create_camper.html', context)

def edit_camper(request, id_camp, id_camper):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    context['id_camper'] = id_camper
    context['campers'] = Camper.objects.filter(pk=id_camper)
    camper = Camper.objects.get(pk=id_camper)
    if id_camp:
        context['active_camp'] = True
    if request.method == 'POST':
        post = request.POST
        user_personal_id = request.user.personal_id
        personal = updatePersonal(post, user_personal_id)
        school = post.get('school')
        parent_phone = post.get('parent_phone')
        parent_name = post.get('parent_name')
        group = post.get('group')

        camper.school = school
        camper.parent_home = parent_home
        camper.parent_name = parent_name
        camper.group = group

        camper.save()

        messages.success(request, 'อัพเดตโปรไฟล์เสร็จสมบูรณ์')
        return HttpResponseRedirect('../../../../camp/%d/campers/'%id_camp)
    else:
        form = CamperForm()
        context['form'] = form
    return render(request, 'edit_camper.html', context)