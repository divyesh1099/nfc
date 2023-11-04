from django.shortcuts import render, redirect
from django.urls import reverse
from doctor.models import *
from patient.models import *
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import timedelta
# Create your views here.
def index(request):
    user=request.user
    doctor=Doctor.objects.get(user=user)
    patient=Patient.objects.get(user=user)
    is_doctor=False
    is_patient=False
    doctor_appointments=None
    patient_appointments=None
    if doctor: 
        is_doctor=True
        doctor_appointments=Appointment.objects.filter(doctor=doctor).order_by('date', 'time')
    if patient:
        is_patient=True
        patient_appointments=Appointment.objects.filter(patient=patient).order_by('date', 'time')
    context={
        'is_doctor':is_doctor, 
        'is_patient':is_patient, 
        'doctor_appointments': doctor_appointments,
        'patient_appointments': patient_appointments,
    }
    return render(request, 'appointment/index.html', context)

@login_required
def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient  # Ensure this is the correct relation to the Patient model
            appointment.status = form.cleaned_data.get('status', 'SCH')
            appointment.save()
            return redirect('appointment:appointment_detail', appointment_id=appointment.pk)
        else:
            print(form.errors) 
    else:
        form = AppointmentForm()
        # You do not need to set 'patient' here since it is handled when saving.

    return render(request, 'appointment/schedule_appointment.html', {'form': form, 'doctors': Doctor.objects.all()})

def appointment_detail(request, appointment_id):
    appointment=Appointment.objects.get(id=appointment_id)
    context={
        'appointment': appointment,
    }
    return render(request, 'appointment/appointment_detail.html', context)