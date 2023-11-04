from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'consultation/index.html')

def virtual_consultation(request):
    return render(request, 'consultation/virtual_consultation.html')