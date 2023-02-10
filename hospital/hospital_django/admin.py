from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Procedure)
admin.site.register(Medication)
admin.site.register(Physician)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Department)
admin.site.register(Block)
admin.site.register(On_call)
admin.site.register(Affiliated_with)
admin.site.register(Trained_in)
admin.site.register(Appointment)
admin.site.register(Prescribe)
admin.site.register(Room)
admin.site.register(Stay)
admin.site.register(Undergo)