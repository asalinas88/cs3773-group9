from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


# Create your models here.
# class EMISUser(AbstractUser):
#     pass


class Patient(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.TextField(max_length=255)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Staff(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
        permissions = [
            ('schedule_appointment', "Can schedule appointments"),
            ('write_prescription', "Can write prescriptions"),
        ]
