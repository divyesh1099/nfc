from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'patient/index.html')

def view_medical_records(request):
    return render(request, 'patient/view_medical_records.html')