from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^home$', views.home, name = "home"),
    url(r'^home/add$', views.add_page, name = "add_page"),
    url(r'^home/process_add$', views.process_add),
    url(r'^home/trip_info/(?P<id>\d+)$', views.trip_info, name = "trip_info")
]
