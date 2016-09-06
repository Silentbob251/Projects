from django import forms
from .models import Patient
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("last_name","first_name","phone_number","phone_type","street1","street2","city","state","zip_zip","second_number","second_type","email", "insurance")
