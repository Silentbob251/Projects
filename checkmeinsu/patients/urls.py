from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.patientview, name='patient'),
    url(r'^create/$', views.create_patient, name='create_patient'),
]
