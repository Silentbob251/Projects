
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.superuser, name='superuser'),
    url(r'^userpage/$', views.userpage, name='userpage'),
    url(r'^configuration/$', views.configuration, name='configuration'),
    url(r'^userform/$', views.userform, name='userform'),
]
