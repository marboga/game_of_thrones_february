from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User, House
from ..regions.models import Region

# Create your views here.
def index(request):
    context = {
        'first_name': 'George',
        'people': User.objects.all(),
        'houses': House.objects.all(),
        'regions': Region.objects.all(),
    }
    return render(request, 'game_of_thrones/index.html', context)

def create_user(request):
    if request.method == 'POST':
        success, returned_data = User.objects.create_new_user(request.POST)

        if success == True:
            request.session.pop('formdata')
            request.session['name'] = returned_data.first_name
            return redirect('house:index')
        else:
            for err in returned_data:
                messages.error(request, err)
            request.session['formdata'] = request.POST

    return redirect('house:index')

def success(request):
    pass

def create_house(request):
    if request.method == 'POST':
        print House.objects.create(
            name=request.POST['name'],
            words=request.POST['words'],
            banner=request.POST['banner'],
            color_1=request.POST['color_1'],
            color_2=request.POST['color_2'],
        )

    return redirect('house:index')
