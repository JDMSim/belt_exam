from django.shortcuts import render, redirect
from .models import Trip
from django.contrib import messages
def index(request):
    if 'user_id' not in request.session:
        return redirect('main:home')

    print request.session['user_id']
    my_trips =  Trip.objects.filter(goers__id = request.session['user_id'])
    others_trips = Trip.objects.all().exclude(planner__id = request.session['user_id'])
    context = {'mines':my_trips, 'others':others_trips}
    temp = Trip.objects.filter(planner__id = 1)
    print temp[0].goers.all()[1].name
    return render(request, 'belt_exam_app/index.html', context)

def add(request):
    return render(request, 'belt_exam_app/add_trip.html')

def add_trip(request):
    new_trip = Trip.objects.add(request.POST, request.session['user_id'])
    if new_trip['status']:
        return redirect('beltexam:home')
    else:
        for error in new_trip['errors']:
            messages.error(request, error)
        return redirect('beltexam:add')

def trip_details(request, id):
    trip_details = Trip.objects.get(id = id)
    context = {'trip_details':trip_details}
    return render(request, 'belt_exam_app/trip_details.html', context)

def join(request, id):
    Trip.objects.join(id, request.session['user_id'])
    return redirect('beltexam:home')
# Create your views here.
