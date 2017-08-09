from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class EMISUser(AbstractUser):
    pass


class Patient(models.Model):

    user = models.OneToOneField(EMISUser, on_delete=models.CASCADE)
    home_address = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Staff(models.Model):

    user = models.OneToOneField(EMISUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
        permissions = [
            ('schedule_appointment', "Can schedule appointments"),
            ('write_prescription', "Can write prescriptions"),
        ]
