from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.travel),
    url(r'^newTrip/$', views.newTrip),
    url(r'^createTrip$', views.createTrip),
    url(r'^destination/(?P<number>\d+)$', views.destination),
    url(r'^addTrip/(?P<number>\d+)$', views.join),
]
