from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^register_user$', views.register_user),
    url(r'^login_user$', views.login_user),
    url(r'^logout_user$', views.logout_user),
]
