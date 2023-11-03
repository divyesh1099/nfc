from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Speciality(models.Model):
    """
    Model to represent the medical speciality of a doctor.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('speciality')
        verbose_name_plural = _('specialties')
        
    def __str__(self):
        return self.name

class Doctor(models.Model):
    """
    Model to represent a doctor within the hospital information system.
    Inherits from AbstractUser to utilize built-in authentication mechanisms.
    """
    # Basic Information
    photo = models.ImageField(upload_to='doctors/photos/', null=True, blank=True)
    phone_number = PhoneNumberField(unique=True, help_text=_('Contact phone number'))
    bio = models.TextField(_('biography'), blank=True)

    # Professional Information
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True)
    license_number = models.CharField(max_length=40, unique=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    education = models.CharField(max_length=255, help_text=_("Doctor's academic degree"))
    languages_spoken = models.CharField(max_length=255, help_text=_("Languages the doctor can speak"))

    # Work Information
    department = models.CharField(max_length=255, help_text=_("Department the doctor belongs to"))
    consultation_hours = models.CharField(max_length=255, help_text=_("Available time slots for consultation"))
    is_consultant = models.BooleanField(default=False, help_text=_("Is the doctor a consultant?"))

    # Compliance and Security
    is_verified = models.BooleanField(default=False, help_text=_('Designates whether the doctor is verified.'))
    verification_document = models.FileField(upload_to='doctors/verification_docs/', null=True, blank=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_full_name()} - {self.speciality}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('doctor_detail', kwargs={'pk': self.pk})