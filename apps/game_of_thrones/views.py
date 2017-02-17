from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User, House, Region

# Create your views here.
def index(request):
    context = {
        'first_name': 'George',
        'people': User.objects.all(),
        'houses': House.objects.all(),
    }
    return render(request, 'game_of_thrones/index.html', context)

def process(request):
    if request.method == 'POST':
        print request.POST, "<<<--- here is post data"

        returned_tuple = User.objects.create_new_user(request.POST)

        print returned_tuple, "this is (boolean, error list or user object)"
        if returned_tuple[0] == True:
            request.session['name'] = returned_tuple[1].first_name
            return redirect('/')
        else:
            for err in returned_tuple[1]:
                messages.error(request, err)

    return redirect('/')

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

    return redirect('/')
