from django import forms
from .models import Medicine, MedicineMedicationSchedule, MedicationSchedule


class MedicationForm(forms.ModelForm):
    # medicationSchedule = forms.ModelMultipleChoiceField(queryset=MedicationSchedule.objects.filter(created_by=request.user))
    # medicationSchedule = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = MedicineMedicationSchedule
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MedicationForm, self).__init__(*args, **kwargs)
        # self.medicationSchedule = 
        self.fields['medicationSchedule'].widget.attrs['readonly'] = True
        # self.fields['medicationSchedule'].queryset = MedicationSchedule.objects.filter(created_by=user).last()
        # self.fields['created_by'].widget.attrs['disabled'] = True
