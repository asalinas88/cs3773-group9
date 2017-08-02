from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Patient(User):

    home_address = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Staff(User):

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
        permissions = [
            ('schedule_appointment', "Can schedule appointments"),
            ('write_prescription', "Can write prescriptions"),
        ]
