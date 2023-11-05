from django.urls import path
from . import views
app_name='appointment'
urlpatterns=[
    path('', views.index, name='index'),
    path('<int:appointment_id>', views.appointment_detail, name='appointment_detail'),
    path('update/<int:pk>', views.appointment_update, name='appointment_update'),
    path('cancel/', views.appointment_cancel, name='appointment_cancel'),
    path('schedule_appointment', views.schedule_appointment, name='schedule_appointment'),
]