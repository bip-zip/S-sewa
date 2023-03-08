from django.contrib import admin
from .models import MedicationSchedule, Medicine, MedicineMedicationSchedule

admin.site.register(MedicineMedicationSchedule)
admin.site.register(MedicationSchedule)
admin.site.register(Medicine)
