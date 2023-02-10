from rest_framework import serializers
from .models import *

class ProcedureSerializer(serializers.HyperlinkedModelSerializer):
    procedure = serializers.HyperlinkedRelatedField(view_name='procedure_detail', read_only=True)
    procedure_url = serializers.ModelSerializer.serializer_url_field(view_name='procedure_detail')
    class Meta:
        model = Procedure
        fields = ('id', 'name', 'cost', 'procedure', 'procedure_url')