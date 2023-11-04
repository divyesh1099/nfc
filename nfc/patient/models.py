from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Patient(models.Model):
    # Basic details
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=30)
    last_name = models.CharField(_("Last Name"), max_length=30)
    date_of_birth = models.DateField(_("Date of Birth"))
    gender = models.CharField(_("Gender"), max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    
    # Contact information
    phone_number = PhoneNumberField(_("Phone Number"), unique=True, help_text=_("Enter patient's contact phone number"))
    email = models.EmailField(_("Email Address"), unique=True)
    address = models.TextField(_("Address"))

    # Unique identification
    aadhar_number = models.CharField(_("Aadhar Number"), max_length=12, unique=True)
    # Aadhar number and other sensitive information should be encrypted - this is just a placeholder.
    
    # Health Information
    blood_type = models.CharField(_("Blood Type"), max_length=3, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')])
    allergies = models.TextField(_("Allergies"), blank=True, help_text=_("List of patient allergies"))
    medical_conditions = models.TextField(_("Medical Conditions"), blank=True, help_text=_("List of current and past medical conditions"))
    
    # Emergency contact
    emergency_contact_name = models.CharField(_("Emergency Contact Name"), max_length=100)
    emergency_contact_phone = PhoneNumberField(_("Emergency Contact Phone"))
    emergency_contact_relation = models.CharField(_("Relationship to Patient"), max_length=50)

    # Profile image
    profile_image = models.ImageField(_("Profile Image"), upload_to='patient_profiles/', null=True, blank=True)

    # Audit fields
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = _("Patient")
        verbose_name_plural = _("Patients")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"