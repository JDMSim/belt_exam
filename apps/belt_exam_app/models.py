from __future__ import unicode_literals
from ..loginRegistration_app.models import User
from datetime import datetime
from django.db import models

class TripManager(models.Manager):
    def add(self, postData, u_id):
        error_list = []
        going = datetime.strptime(postData['start'], '%Y-%m-%d')
        coming = datetime.strptime(postData['end'], '%Y-%m-%d')
        now = datetime.now()

        if going < now:
            error_list.append('Departure date must in the future')
            context = {'status':0, 'errors':error_list}
            return context

        if coming < going:
            error_list.append('Arrival date must after Departure')
            context = {'status':0, 'errors':error_list}
            return context

        user = User.objects.get(id = u_id)
        self.create(destination = postData['dest'], description =  postData['desc'], start_date =  postData['start'], end_date =  postData['end'], planner = user)
        trip_row = self.order_by('-id')[0]
        trip = self.get(id = trip_row.id)
        trip.goers.add(user)
        context = {'status':1}
        return context

    def join(self, t_id, u_id):
        user = User.objects.get(id = u_id)
        trip = self.get(id = t_id)
        trip.goers.add(user)


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    planner = models.ForeignKey(User)
    goers = models.ManyToManyField(User, related_name = 'all_users')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = TripManager()
# Create your models here.
