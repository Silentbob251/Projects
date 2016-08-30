from django.shortcuts import render
from .models import Patient

def patientview(request):
    patients = Patient.objects.all()
    return render(request, "patient.html", {'patients':patients})
# Create your views here.
