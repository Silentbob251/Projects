from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import PatientForm, DeleteNewForm
from .models import Patient


def patientview(request):
    patients=Patient.objects.all()
    return render(request, "patient.html", {'patients':patients})


def create_patient(request):
    if request.method=="GET":
        form=PatientForm()
        return render(request, "create_patient.html", {'form': form})

    elif request.method =="POST":
        form=PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("patients:patient")

        else:
            return render(request, "create_patient.html", {'form': form})


def patient_detail(request, patient_id):
    patient=get_object_or_404(Patient, id=patient_id)
    return render(request, "patient_detail.html", {'patient':patient})


def edit_patient(request, patient_id):
    if request.method=='GET':
        patient=get_object_or_404(Patient, id=patient_id)
        form=PatientForm(instance=patient)
        return render(request, "edit_patient.html", {'form': form, 'patient':patient})

    elif request.method=='POST':
        patient=get_object_or_404(Patient, id=patient_id)
        form=PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            return redirect("patients:patient_detail", patient.id)

        else:
            return render(request, "edit_patient.html", {'form': form})


def delete_patient(request, patient_id):
    patient=get_object_or_404(Patient, id=patient_id)

    if request.method=='POST':
        form=DeleteNewForm(request.POST, instance=patient)

        if form.is_valid():
            patient.delete()
            return HttpResponseRedirect("/")

    else:
        form = DeleteNewForm(instance=patient)
        return HttpResponseRedirect("/patients/")
        #return render({'patients': patient})

# Create your views here.
