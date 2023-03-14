from django import forms
from .models import HealthRecord

class RecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['prescription','status','documents','end_date']
        widgets = {
            'end_date':forms.DateInput(attrs={'type': 'date'})
        }
        