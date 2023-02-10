from rest_framework import serializers
from .models import *

class ProcedureSerializer(serializers.HyperlinkedModelSerializer):
    procedure = serializers.HyperlinkedRelatedField(view_name='procedure_detail', read_only=True)
    procedure_url = serializers.ModelSerializer.serializer_url_field(view_name='procedure_detail')
    class Meta:
        model = Procedure
        fields = ('id', 'name', 'cost', 'procedure', 'procedure_url')

class MedicationSerializer(serializers.HyperlinkedModelSerializer):
    medication_url = serializers.ModelSerializer.serializer_url_field(view_name='medication_detail')
    class Meta:
        model = Medication
        fields = ('id', 'name', 'brand', 'description', 'medication_url')

class PhysicianSerializer(serializers.HyperlinkedModelSerializer):
    physician_url = serializers.ModelSerializer.serializer_url_field(view_name='physician_detail')
    class Meta:
        model = Physician
        fields = ('id', 'name', 'position', 'ssn', 'physician_url')

class NurseSerializer(serializers.HyperlinkedModelSerializer):
    nurse_url = serializers.ModelSerializer.serializer_url_field(view_name='nurse_detail')
    class Meta:
        model = Nurse
        fields = ('id', 'name', 'position', 'registered', 'ssn', 'nurse_url')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    pcp = serializers.HyperlinkedRelatedField(view_name='physician_detail', read_only=True)
    pcp_id = serializers.PrimaryKeyRelatedField(
        queryset=Physician.objects.all(),
        source='pcp'
    )
    patient_url = serializers.ModelSerializer.serializer_url_field(view_name='patient_detail')
    class Meta:
        model = Patient
        fields = ('id', 'name', 'address', 'phone', 'insurance_id', 'ssn', 'pcp', 'pcp_id', 'patient_url')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    physician = serializers.HyperlinkedRelatedField(view_name='physician_detail', read_only=True)
    physician_id = serializers.PrimaryKeyRelatedField(
        queryset=Physician.objects.all(),
        source='head'
    )
    department_url = serializers.ModelSerializer.serializer_url_field(view_name='department_detail')
    class Meta:
        model = Department
        fields = ('id', 'name', 'physician', 'physician_id', 'department_url')

class BlockSerializer(serializers.HyperlinkedModelSerializer):
    block_url = serializers.ModelSerializer.serializer_url_field(view_name='block_detail')
    class Meta:
        model = Block
        fields = ('id', 'block_floor', 'block_code', 'block_url')

class On_callSerializer(serializers.HyperlinkedModelSerializer):
    nurse = serializers.HyperlinkedRelatedField(view_name='nurse_detail', read_only=True)
    nurse_id = serializers.PrimaryKeyRelatedField(
        queryset=Nurse.objects.all(),
        source='nurse'
    )
    block = serializers.HyperlinkedRelatedField(view_name='block_detail', read_only=True)
    block_id = serializers.PrimaryKeyRelatedField(
        queryset=Block.objects.all(),
        source='block'
    )
    on_call_url = serializers.ModelSerializer.serializer_url_field(view_name='on_call_detail')
    class Meta:
        model = On_call
        fields = ('id', 'nurse', 'nurse_id', 'block', 'block_id', 'on_call_start', 'on_call_end', 'on_call_url')

class Affiliated_withSerializer(serializers.HyperlinkedModelSerializer):
    physician = serializers.HyperlinkedRelatedField(view_name='physician_detail', read_only=True)
    physician_id = serializers.PrimaryKeyRelatedField(
        queryset=Physician.objects.all(),
        source='physician'
    )
    department = serializers.HyperlinkedRelatedField(view_name='department_detail', read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department'
    )
    affiliated_with_url = serializers.ModelSerializer.serializer_url_field(view_name='affiliated_with_detail')
    class Meta:
        model = Affiliated_with
        fields = ('id', 'physician', 'physician_id', 'department', 'department_id', 'primary_affiliation', 'affiliated_with_url')

class Trained_inSerializer(serializers.HyperlinkedModelSerializer):
    physician = serializers.HyperlinkedRelatedField(view_name='physician_detail', read_only=True)
    physician_id = serializers.PrimaryKeyRelatedField(
        queryset=Physician.objects.all(),
        source='physician'
    )
    treatment = serializers.HyperlinkedRelatedField(view_name='procedure_detail', read_only=True)
    treatment_id = serializers.PrimaryKeyRelatedField(
        queryset=Procedure.objects.all(),
        source='treatment'
    )
    trained_in_url = serializers.ModelSerializer.serializer_url_field(view_name='trained_in_detail')
    class Meta:
        model = Trained_in
        fields = ('id', 'physician', 'physician_id', 'treatment', 'treatment_id', 'certification_date', 'certification_exp', 'trained_in_url')

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(view_name='patient_detail', read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(),
        source='patient'
    )
    prep_nurse = serializers.HyperlinkedRelatedField(view_name='nurse_detail', read_only=True)
    prep_nurse_id = serializers.PrimaryKeyRelatedField(
        queryset=Nurse.objects.all(),
        source='prep_nurse'
    )
    physician = serializers.HyperlinkedRelatedField(view_name='physician_detail', read_only=True)
    physician_id = serializers.PrimaryKeyRelatedField(
        queryset=Physician.objects.all(),
        source='physician'
    )
    appointment_url = serializers.ModelSerializer.serializer_url_field(view_name='appointment_detail')
    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'patient_id', 'prep_nurse', 'prep_nurse_id', 'physician', 'physician_id', 'start_dt_time', 'end_dt_time', 'examination_room', 'appointment_url')

class PrescribeSerializer(serializers.HyperlinkedModelSerializer):
    physician = serializers.HyperlinkedRelatedField(view_name='physician_detail', read_only=True)
    physician_id = serializers.PrimaryKeyRelatedField(
        queryset=Physician.objects.all(),
        source='physician'
    )
    patient = serializers.HyperlinkedRelatedField(view_name='patient_detail', read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(),
        source='patient'
    )
    medication = serializers.HyperlinkedRelatedField(view_name='medication_detail', read_only=True)
    medication_id = serializers.PrimaryKeyRelatedField(
        queryset=Medication.objects.all(),
        source='medication'
    )
    appointment = serializers.HyperlinkedRelatedField(view_name='appointment_detail', read_only=True)
    appointment_id = serializers.PrimaryKeyRelatedField(
        queryset=Appointment.objects.all(),
        source='appointment'
    )
    prescribe_url = serializers.ModelSerializer.serializer_url_field(view_name='prescribe_detail')
    class Meta:
        model = Prescribe
        fields = ('id', 'physician', 'physician_id', 'patient', 'patient_id', 'medication', 'medication_id', 'appointment', 'appointment_id', 'date', 'dose', 'prescribe_url')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    block = serializers.HyperlinkedRelatedField(view_name='block_detail', read_only=True)
    block_id = serializers.PrimaryKeyRelatedField(
        queryset=Block.objects.all(),
        source='block'
    )
    room_url = serializers.ModelSerializer.serializer_url_field(view_name='room_detail')
    class Meta:
        model = Room
        fields = ('id', 'block', 'block_id', 'room_type', 'unavailable', 'room_url')

class StaySerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(view_name='patient_detail', read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(),
        source='patient'
    )
    room = serializers.HyperlinkedRelatedField(view_name='room_detail', read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(),
        source='room'
    )
    stay_url = serializers.ModelSerializer.serializer_url_field(view_name='stay_detail')
    class Meta:
        model = Stay
        fields = ('id', 'patient', 'patient_id', 'room', 'room_id', 'start_time', 'end_time', 'stay_url')

class UndergoSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.HyperlinkedRelatedField(view_name='patient_detail', read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(),
        source='patient'
    )
    procedure = serializers.HyperlinkedRelatedField(view_name='procedure_detail', read_only=True)
    procedure_id = serializers.PrimaryKeyRelatedField(
        queryset=Procedure.objects.all(),
        source='procedure'
    )
    stay = serializers.HyperlinkedRelatedField(view_name='stay_detail', read_only=True)
    stay_id = serializers.PrimaryKeyRelatedField(
        queryset=Stay.objects.all(),
        source='stay'
    )
    physician = serializers.HyperlinkedRelatedField(view_name='physician_detail', read_only=True)
    physician_id = serializers.PrimaryKeyRelatedField(
        queryset=Physician.objects.all(),
        source='physician'
    )
    assisting_nurse = serializers.HyperlinkedRelatedField(view_name='nurse_detail', read_only=True)
    assisting_nurse_id = serializers.PrimaryKeyRelatedField(
        queryset=Nurse.objects.all(),
        source='assisting_nurse'
    )
    undergo_url = serializers.ModelSerializer.serializer_url_field(view_name='undergo_detail')
    class Meta:
        model = Undergo
        fields = ('id', 'patient', 'patient_id', 'procedure', 'procedure_id', 'stay', 'stay_id', 'physician', 'physician_id', 'assisting_nurse', 'assisting_nurse_id', 'date', 'undergo_url')