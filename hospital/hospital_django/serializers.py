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