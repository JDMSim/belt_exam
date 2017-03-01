from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^add$', views.add, name = 'add'),
    url(r'^add_trip$', views.add_trip, name = 'add_trip'),
    url(r'trip_details/(?P<id>\d+)$', views.trip_details, name = 'trip_details'),
    url(r'join/(?P<id>\d+)$', views.join, name = 'join')
]
