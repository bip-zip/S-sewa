from django.urls import path
from .views import MedicationListView

app_name = 'medication'
urlpatterns = [
    path('', MedicationListView.as_view(), name='medicationlist' ),
  
]
