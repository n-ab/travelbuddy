from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    print('------------ENTERING INDEX-----------')
    return render(request, 'login/index.html')

def register_user(request):
    if request.method == 'POST':
        print('------------ATTEMPTING REGISTER-----------')
        print(request.POST)
        response_from_models = User.objects.user_manager(request.POST)
        print(response_from_models)
        if response_from_models['status']:
            print('------------RETURNED TO VIEWS')
            request.session['user'] = response_from_models['user']
            print('------------request.session.user CREATED')
            print(request.session['user'])
            return redirect('login:index')
        else:
            for error in response_from_models['errors']:
                messages.error(request, error)
            return redirect('login:index')

def login_user(request):
        response_from_models = User.objects.login_user(request.POST)
        print(response_from_models)
        if response_from_models['status']:
            request.session['user_id'] = response_from_models['user'].id
            print('-------------------PRINTING SESSION')
            print(request.session['user_id'])
            # context = {
            #     'user': User.objects.get(id=request.session['user_id'])
            # }
            context = {
                'user': User.objects.get(id=request.session['user_id'])
            }
            print(context)
            print('********CHANGE YOUR REDIRECT*********')
            return redirect('travel:home')

        else:
            messages.error(request, response_from_models['errors'])
            return redirect('login:index')


def logout_user(request):
    if request.method == 'POST':
        print('user_id', '=', request.session['user_id'])
        request.session.clear()
        print('---------SESSION CLEARED----------')
    return redirect('login:index')
