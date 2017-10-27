from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Destination
from ..login.models import User

def home(request):
    print('-----------ENTER HOME----------')
    user_id = request.session['user_id']
    context = {
        'user_list': User.objects.filter(id=request.session['user_id']),
        'travel_list': Destination.objects.all().values(),
    }
    return render(request, 'travel/home.html', context)

def add_page(request):
    print('-----------ENTER ADD PAGE----------')
    return render(request, 'travel/add.html')

def process_add(request):
    if request.method == 'POST':
        response_from_models = Destination.objects.d_manager(request.POST)
        if response_from_models['status']:
            return redirect('travel:home')
        else:
            for error in response_from_models['errors']:
                messages.error(request, error)
            return redirect('travel:addpage')

def trip_info(request, id):
    print('-----------ENTER INFO----------')
    context = {
        'users':User.objects.all().values(),
        'destinations':Destination.objects.filter(id=id)
    }
    return render(request, 'travel/trip_info.html', context)
