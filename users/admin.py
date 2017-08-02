from django.contrib import admin
from .models import Patient, Staff


# Register the Admin classes for Patient using the decorator
@admin.register(Patient)
class StaffAdmin(admin.ModelAdmin):
    pass


# Register the Admin classes for Staff using the decorator
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass
