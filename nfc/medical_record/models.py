from django.db import models
from patient.models import Patient
from django.utils.translation import gettext_lazy as _

class MedicalRecord(models.Model):
    # Link to the Patient model
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, verbose_name=_("Patient's Medical Record"))
    
    # Unique identifier for the medical record
    record_number = models.CharField(_("Record Number"), max_length=50, unique=True)
    
    # Comprehensive medical history
    medical_history = models.TextField(_("Medical History"), blank=True, help_text=_("Detailed medical history of the patient"))
    
    # List of current medications
    current_medications = models.TextField(_("Current Medications"), blank=True, help_text=_("Current medications the patient is taking"))
    
    # List of surgical history
    surgical_history = models.TextField(_("Surgical History"), blank=True, help_text=_("Past surgical procedures"))
    
    # Family medical history
    family_history = models.TextField(_("Family Medical History"), blank=True, help_text=_("Family medical history relevant to patient's health"))
    
    # Immunization records
    immunizations = models.TextField(_("Immunization Records"), blank=True, help_text=_("Record of immunizations and vaccinations"))
    
    # Social history including smoking, alcohol use, etc.
    social_history = models.TextField(_("Social History"), blank=True, help_text=_("Information on lifestyle factors such as smoking, alcohol use, etc."))
    
    # Chronic conditions like diabetes, hypertension, etc.
    chronic_conditions = models.TextField(_("Chronic Conditions"), blank=True, help_text=_("List of chronic conditions the patient has been diagnosed with"))
    
    # List of allergies including drug, food, and environmental
    detailed_allergies = models.TextField(_("Detailed Allergies"), blank=True, help_text=_("Detailed list of allergies"))
    
    # Regularly recorded vital signs like blood pressure, heart rate, etc.
    vital_signs = models.TextField(_("Vital Signs"), blank=True, help_text=_("History of vital signs like blood pressure, heart rate, etc."))
    
    # Living wills, health care proxies, or advanced directives
    advanced_directives = models.TextField(_("Advanced Directives"), blank=True, help_text=_("Information on living wills, health care proxies, or advanced directives"))
    
    # Laboratory test results
    lab_results = models.TextField(_("Laboratory Results"), blank=True, help_text=_("Summary of laboratory test results"))
    
    # Radiology images and reports
    radiology_reports = models.TextField(_("Radiology Reports"), blank=True, help_text=_("Radiology images and reports"))
    
    # Special notes by healthcare providers
    provider_notes = models.TextField(_("Provider Notes"), blank=True, help_text=_("Special notes made by healthcare providers"))
    
    # Audit fields
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = _("Medical Record")
        verbose_name_plural = _("Medical Records")

    def __str__(self):
        return f"Medical Record {self.record_number} - {self.patient}"

# You would create a new Django app called 'medical_records' and place this model inside its models.py file.
