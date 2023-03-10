from django.urls import path
from .views import MedicationListView, AddMedicationSchedule
from . import views
app_name = 'medication'
urlpatterns = [
    path('', MedicationListView.as_view(), name='medicationlist' ),
    path('add/', AddMedicationSchedule.as_view(), name='addmedication' ),
    path('medicationcreate/', views.medicationScheduleCreator, name='createmedication' ),
    # path('<str:qrdata>/add', AddMedicationSchedule.as_view(), name='addmedication' ),
  
]
