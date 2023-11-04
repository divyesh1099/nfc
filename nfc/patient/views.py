from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required
def index(request):
    patient_profile = Patient.objects.get(user=request.user)
    patient_id = patient_profile.id
    context={
        'patient_id': patient_id,
    }
    return render(request, 'patient/index.html', context)