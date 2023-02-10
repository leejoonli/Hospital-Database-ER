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
]