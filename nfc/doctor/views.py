from django.shortcuts import render
from appointment.models import *
from datetime import date
# Create your views here.
def index(request):
    doctor = request.user.doctor
    appointments_today = Appointment.objects.filter(doctor=doctor, date=date.today())
    context = {
        'appointments_today': appointments_today,
        'number_of_appointments': appointments_today.count(), 
    }
    return render(request, 'doctor/index.html', context)