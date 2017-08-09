from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Patient(User):
    home_address = models.TextField(max_length=255)

    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='file')

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        db_table = 'file'


class Staff(User):

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
        permissions = [
            ('schedule_appointment', "Can schedule appointments"),
            ('write_prescription', "Can write prescriptions"),
        ]
