# Generated by Django 4.2.7 on 2023-11-04 16:22

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, verbose_name='Gender')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text="Enter patient's contact phone number", max_length=128, region=None, unique=True, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('address', models.TextField(verbose_name='Address')),
                ('aadhar_number', models.CharField(max_length=12, unique=True, verbose_name='Aadhar Number')),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, verbose_name='Blood Type')),
                ('allergies', models.TextField(blank=True, help_text='List of patient allergies', verbose_name='Allergies')),
                ('medical_conditions', models.TextField(blank=True, help_text='List of current and past medical conditions', verbose_name='Medical Conditions')),
                ('emergency_contact_name', models.CharField(max_length=100, verbose_name='Emergency Contact Name')),
                ('emergency_contact_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Emergency Contact Phone')),
                ('emergency_contact_relation', models.CharField(max_length=50, verbose_name='Relationship to Patient')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='patient_profiles/', verbose_name='Profile Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
        ),
    ]