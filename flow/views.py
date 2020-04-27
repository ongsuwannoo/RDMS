from django.shortcuts import render
from index.views import getPersonal
from locations.models import Location

# Create your views here.

def flow(request, id_camp):
    context = getPersonal(request)
    context['id_camp'] = id_camp
    if id_camp:
        context['active_camp'] = True
    
    if request.method == 'POST':
        post = request.POST
        time = post.get(time).split('-')
        time_start = time[0]
        time_end = time[1]
        activity = post.get('activity')
        sub_time = post.get('sub_time')
        desc = post.get('desc')
        department = post.get('department')
        mc = post.get('department')
        location = post.get('location')
        note = post.get('note')
    else:
        context['location'] = Locations.objects.all()
        # context['department'] = Department.

    return render(request, 'flow.html', context)