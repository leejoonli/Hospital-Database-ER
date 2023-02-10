from django.urls import path
from . import views
#from rest_framework import DefaultRouter

urlpatterns = [
    path('procedures', views.ProcedureList.as_view(), name='procedure_list'),
    path('procedures/<int:pk>', views.ProcedureDetail.as_view(), name='procedure_detail'),
    path('medications', views.MedicationList.as_view(), name='medication_list'),
    path('medications/<int:pk>', views.MedicationDetail.as_view(), name='medication_detail'),
    path('physicians', views.PhysicianList.as_view(), name='physician_list'),
    path('physicians/<int:pk>', views.PhysicianDetail.as_view(), name='physician_detail'),
    path('nurses', views.NurseList.as_view(), name='nurse_list'),
    path('nurses/<int:pk>', views.NurseDetail.as_view(), name='nurse_detail'),
    path('patients', views.PatientList.as_view(), name='patient_list'),
    path('patients/<int:pk>', views.PatientDetail.as_view(), name='patient_detail'),
    path('departments', views.DepartmentList.as_view(), name='department_list'),
    path('departments/<int:pk>', views.DepartmentDetail.as_view(), name='department_detail'),
    path('blocks', views.BlockList.as_view(), name='block_list'),
    path('blocks/<int:pk>', views.BlockDetail.as_view(), name='block_detail'),
    path('on_calls', views.On_callList.as_view(), name='on_call_list'),
    path('on_calls/<int:pk>', views.On_callDetail.as_view(), name='on_call_detail'),
    path('affiliated_withs', views.Affiliated_withList.as_view(), name='affiliated_with_list'),
    path('affiliated_withs/<int:pk>', views.Affiliated_withDetail.as_view(), name='affiliated_with_detail'),
    path('trained_ins', views.Trained_inList.as_view(), name='trained_in_list'),
    path('trained_ins/<int:pk>', views.Trained_inDetail.as_view(), name='trained_in_detail'),
    path('appointments', views.AppointmentList.as_view(), name='appointment_list'),
    path('appointments/<int:pk>', views.AppointmentDetail.as_view(), name='appointment_detail'),
    path('prescribes', views.PrescribeList.as_view(), name='prescribe_list'),
    path('prescribes/<int:pk>', views.PrescribeDetail.as_view(), name='prescribe_detail'),
]