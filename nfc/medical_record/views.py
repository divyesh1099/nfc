from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import MedicalRecord
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def index(request, patient_id):
    medical_record = MedicalRecord.objects.get(patient__id=patient_id)
    context={
        'medical_record': medical_record,
    }
    return render(request, 'medical_record/index.html', context)

@login_required
def download_medical_record(request, record_number):
    # Retrieve the medical record using the unique record_number
    medical_record = get_object_or_404(MedicalRecord, record_number=record_number)

    # Assert that the request.user is the patient or the doctor who has access
    if request.user != medical_record.patient.user and not request.user.is_doctor:
        return HttpResponse("Unauthorized", status=401)

    # Use a Django template to generate HTML content for the PDF
    template_path = 'medical_record/download_template.html'
    context = {'medical_record': medical_record}
    # Load the template and render it with the medical record context
    template = get_template(template_path)
    html = template.render(context)

    # Create a Django HttpResponse object, and set the content_type as PDF
    response = HttpResponse(content_type='application/pdf')
    # If download, set the Content-Disposition header
    response['Content-Disposition'] = f'attachment; filename="Medical_Record_{record_number}.pdf"'

    # Create the PDF
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )

    # If there was an error in creating the PDF, return an appropriate response
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response