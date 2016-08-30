from django.db import models

class Patient(models.Model):
    #required
    last_name = models.CharField(max_length=50)
    first_name =  models.CharField(max_length=50)
    phone_number =  models.CharField(max_length=50)
    phone_type =  models.CharField(max_length=50)

    #optional
    street1 =  models.CharField(max_length=150, blank=True)
    street2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_zip = models.CharField(max_length=5, blank=True)
    second_number = models.CharField(max_length=50, blank=True)
    second_type = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank = True)
    insurance = models.CharField(max_length=50, blank=True)


# Create your models here.
