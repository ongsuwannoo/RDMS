from datetime import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from index.views import (Personal, getPersonal, group_required, savePersonal,
                         updatePersonal)
from personal.models import Personal

from .forms import *
from personal.views import*
from .models import Camper, Observe
import csv, io
# Create your views here.


def campers(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    context['campers'] = reversed(Camper.objects.select_related('personal').filter(camp_id=id_camp))
    if id_camp:
        context['active_camp'] = True
    return render(request, 'campers.html', context)

@group_required('manager', 'head', 'staff')
def camper_detail(request, id_camp, id_camper):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    context['id_camper'] = id_camper
    context['name'] = getPersonal(request)['name']
    context['campers'] = Camper.objects.filter(id=id_camper)
    context['observe'] = Observe.objects.filter(camper_id = id_camper)
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

@group_required('manager')
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

@group_required('manager')
def edit_camper(request, id_camp, id_camper):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    context['id_camper'] = id_camper
    context['campers'] = Camper.objects.filter(pk=id_camper)
    camper = Camper.objects.get(pk=id_camper)
    print(camper.personal_id)
    if id_camp:
        context['active_camp'] = True
    if request.method == 'POST':
        post = request.POST
        personal_id = camper.personal_id
        print(personal_id)
        personal = updatePersonal(post, personal_id)
        school = post.get('school')
        parent_phone = post.get('parent_phone')
        parent_name = post.get('parent_name')
        group = post.get('group')

        camper.school = school
        camper.parent_phone = parent_phone
        camper.parent_name = parent_name
        camper.group = group

        camper.save()

        messages.success(request, 'อัพเดตโปรไฟล์เสร็จสมบูรณ์')
        return HttpResponseRedirect('../../../../%d/campers/'%id_camp)
    else:
        form = CamperForm()
        context['form'] = form
    return render(request, 'edit_camper.html', context)

@group_required('manager')
def delete_camper(request, id_camp, id_camper=""):
    context = getPersonal(request)
    context['id_camp'] = id_camp

    camper = Camper.objects.get(pk=id_camper)
    camper.delete()
    messages.warning(request, 'ลบ '+camper.personal.first_name+' '+camper.personal.last_name+' เรียบร้อย')
    return HttpResponseRedirect('../../../../%d/campers' % id_camp)

@group_required('staff')
def add_observe(request, id_camp, id_camper):
    context = {}
    context['id_camp'] = id_camp
    context['id_camper'] = id_camper
    context['name'] = getPersonal(request)['name']
    context['observes'] = Observe.objects.filter(camper_id = id_camper)
    
    if request.method == 'POST':
        split_second = str(datetime.now().time()).split('.')[0]
        time = str(datetime.now().date()) +' ' + split_second
        observe = request.POST.get('observe')
        observe_object = Observe(
            text = observe,
            time = time,
            camper_id = id_camper
            )
        observe_object.save()

    return render(request, 'camper_detail.html', context)

@group_required('manager')
def import_camper(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True
    template = "import_camper.html"

    camp = Camp.objects.get(pk=id_camp)
    data = Camper.objects.all()
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        count = 0
        # for _ in range(200):
        #     personal = savePersonal(randomPersonal())
        #     rand = randomCamper()
        #     camper = Camper(
        #         camp = camp,
        #         personal = personal,
        #         school = rand['school'],
        #         parent_phone = rand['parent_phone'],
        #         parent_name = rand['parent_name'],
        #         group = rand['group']
        #     )
        #     camper.save()
        #     count += 1
        #     print('save camper', count)
        messages.warning(request, 'ทำการ import camper จำนวน '+str(count)+' คน หากผิดพลาดโปรดติดต่อผู้ดูแล')
        return render(request, template, context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
        
    data_set = csv_file.read().decode('utf-8-sig')
    dic = csv.DictReader(io.StringIO(data_set), delimiter=",")
    
    # นับจำนวน camper ทั้งหมด
    count = 0
    for i in dic:
        # i.update((k, [v]) for k, v in i.items())

        personal = savePersonal(i)
        school = i['school']
        parent_phone = i['parent_phone']
        parent_name = '-'
        group = i['group']

        camper = Camper(
            camp = camp,
            personal = personal,
            school = school,
            parent_phone = parent_phone,
            parent_name = parent_name,
            group = group
        )

        camper.save()
        count += 1
    messages.warning(request, 'ทำการ import camper จำนวน '+str(count)+' คน หากผิดพลาดโปรดติดต่อผู้ดูแล')
    return HttpResponseRedirect('../../../../camp/%d/campers/'%id_camp)

