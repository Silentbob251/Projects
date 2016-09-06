from django.shortcuts import redirect, render
from .forms import PatientForm
from .models import Patient

def patientview(request):
    patients = Patient.objects.all()
    return render(request, "patient.html", {'patients':patients})

def create_patient(request):
    if request.method == "GET":
        form = PatientForm()
        return render(request, "create_patient.html", {'form': form})
    elif request.method =="POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patients:patient")
        else:
            return render(request, "create_patient.html", {'form': form})
# Create your views here.
