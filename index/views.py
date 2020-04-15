from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index/index.html', context)

    # idcard_value = # something Integer
    # idcard = Idcard(
    #     user_idcard = request.user,
    #     idcard = idcard_value
    # )
    # idcard.save()