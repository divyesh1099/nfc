from django import forms
from .models import Appointment
from datetime import timedelta
from doctor.models import *
class AppointmentForm(forms.ModelForm):
    duration = forms.DurationField(widget=forms.HiddenInput(), initial=timedelta(minutes=30), required=False)
    status = forms.CharField(widget=forms.HiddenInput(), initial='SCH', required=False)

    class Meta:
        model = Appointment
        exclude = ('patient',)  # 'patient' is handled in the view
        fields = '__all__'  # This should probably be removed since 'exclude' is used

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        # Remove 'patient' from validation since it's handled in the view
        self.fields.pop('patient', None)