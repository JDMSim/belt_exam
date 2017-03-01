from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'loginRegistration_app/index.html')

def register(request):
    reg_results = User.objects.Register(request.POST['name'], request.POST['uname'], request.POST['pword'], request.POST['c_pword'])

    if reg_results['status']:
        request.session['user_id'] = reg_results['response'].id
        request.session['name'] = reg_results['response'].name
        request.session['from'] = 'registered'
        return redirect('beltexam:home')
    else:
        for error in  reg_results['response']:
            messages.error(request, error)
        return redirect('main:home')

def login(request):
    myLogin = User.objects.login(request.POST)

    if myLogin['status']:
        request.session['user_id'] = myLogin['response'].id
        request.session['name'] = myLogin['response'].name
        request.session['from'] = 'logged in'
        return redirect('beltexam:home')
    else:
        for error in myLogin['response']:
            messages.error(request, error)
        return redirect('main:home')

def logout(request):
    request.session.clear()
    return redirect('main:home')
