from django.conf.urls import url
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^$', views.patientview, name='patient'),
    url(r'^create/$', views.create_patient, name='create_patient'),
    url(r'^(?P<patient_id>\d+)/$', views.patient_detail, name='patient_detail'),
    url(r'^(?P<patient_id>\d+)/edit/$', views.edit_patient, name='edit_patient'),
    url(r'^(?P<patient_id>\d+)/delete/$', views.delete_patient, name='delete_patient'),
]
