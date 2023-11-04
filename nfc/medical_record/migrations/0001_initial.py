# Generated by Django 4.2.7 on 2023-11-04 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_number', models.CharField(max_length=50, unique=True, verbose_name='Record Number')),
                ('medical_history', models.TextField(blank=True, help_text='Detailed medical history of the patient', verbose_name='Medical History')),
                ('current_medications', models.TextField(blank=True, help_text='Current medications the patient is taking', verbose_name='Current Medications')),
                ('surgical_history', models.TextField(blank=True, help_text='Past surgical procedures', verbose_name='Surgical History')),
                ('family_history', models.TextField(blank=True, help_text="Family medical history relevant to patient's health", verbose_name='Family Medical History')),
                ('immunizations', models.TextField(blank=True, help_text='Record of immunizations and vaccinations', verbose_name='Immunization Records')),
                ('social_history', models.TextField(blank=True, help_text='Information on lifestyle factors such as smoking, alcohol use, etc.', verbose_name='Social History')),
                ('chronic_conditions', models.TextField(blank=True, help_text='List of chronic conditions the patient has been diagnosed with', verbose_name='Chronic Conditions')),
                ('detailed_allergies', models.TextField(blank=True, help_text='Detailed list of allergies', verbose_name='Detailed Allergies')),
                ('vital_signs', models.TextField(blank=True, help_text='History of vital signs like blood pressure, heart rate, etc.', verbose_name='Vital Signs')),
                ('advanced_directives', models.TextField(blank=True, help_text='Information on living wills, health care proxies, or advanced directives', verbose_name='Advanced Directives')),
                ('lab_results', models.TextField(blank=True, help_text='Summary of laboratory test results', verbose_name='Laboratory Results')),
                ('radiology_reports', models.TextField(blank=True, help_text='Radiology images and reports', verbose_name='Radiology Reports')),
                ('provider_notes', models.TextField(blank=True, help_text='Special notes made by healthcare providers', verbose_name='Provider Notes')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.patient', verbose_name="Patient's Medical Record")),
            ],
            options={
                'verbose_name': 'Medical Record',
                'verbose_name_plural': 'Medical Records',
            },
        ),
    ]