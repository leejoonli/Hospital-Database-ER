from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
class ProcedureList(generics.ListCreateAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

class ProcedureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

class MedicationList(generics.ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class MedicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class PhysicianList(generics.ListCreateAPIView):
    queryset = Physician.objects.all()
    serializer_class = PhysicianSerializer

class PhysicianDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Physician.objects.all()
    serializer_class = PhysicianSerializer

class NurseList(generics.ListCreateAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

class NurseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class BlockList(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

class BlockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

class On_callList(generics.ListCreateAPIView):
    queryset = On_call.objects.all()
    serializer_class = On_callSerializer

class On_callDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = On_call.objects.all()
    serializer_class = On_callSerializer

class Affiliated_withList(generics.ListCreateAPIView):
    queryset = Affiliated_with.objects.all()
    serializer_class = Affiliated_withSerializer

class Affiliated_withDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Affiliated_with.objects.all()
    serializer_class = Affiliated_withSerializer

class Trained_inList(generics.ListCreateAPIView):
    queryset = Trained_in.objects.all()
    serializer_class = Trained_inSerializer

class Trained_inDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trained_in.objects.all()
    serializer_class = Trained_inSerializer

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class PrescribeList(generics.ListCreateAPIView):
    queryset = Prescribe.objects.all()
    serializer_class = PrescribeSerializer

class PrescribeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescribe.objects.all()
    serializer_class = PrescribeSerializer