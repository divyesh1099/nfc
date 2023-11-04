from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'appointment/index.html')

def schedule_appointment(request):
    return render(request, 'appointment/schedule_appointment.html')