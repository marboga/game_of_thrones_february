from django.shortcuts import render, redirect

# Create your views here.
from models import Region

def index(request):
    print "in region:index method"
    return render(request, 'regions/index.html')

def create_region(request):
    print "creating region"
    print Region.objects.create(
        name=request.POST['name'],
        climate=request.POST['climate'],
        known_for=request.POST['known_for'],
    )
    return redirect('region:index')
