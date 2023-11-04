from django.db import models
from datetime import timedelta
from patient.models import *
from doctor.models import Doctor
# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Patient", related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Doctor", related_name='doctor_appointments')
    # Appointment Time Information
    date = models.DateField("Appointment Date")
    time = models.TimeField("Appointment Time")
    # Appointment Creation and Modification Timestamps
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)
    # Appointment Status - for example, 'Scheduled', 'Completed', 'Cancelled', etc.
    STATUS_CHOICES = [
        ('SCH', 'Scheduled'),
        ('COM', 'Completed'),
        ('CAN', 'Cancelled'),
        ('RES', 'Rescheduled'),
    ]
    status = models.CharField(
        "Status",
        max_length=3,
        choices=STATUS_CHOICES,
        default='SCH',
    )
    # Additional notes or comments for the appointment
    notes = models.TextField("Notes", blank=True, null=True)

    def __str__(self):
        return f"{self.patient}'s appointment with {self.doctor} on {self.date} at {self.time}"

    class Meta:
        ordering = ['date', 'time']
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        unique_together = [['patient', 'date', 'time']]  # Ensuring a patient doesn't have overlapping appointments
    
    # If you still need to work with the duration conceptually, you could add a method
    def get_duration(self):
        return timedelta(minutes=30)  # Fixed value