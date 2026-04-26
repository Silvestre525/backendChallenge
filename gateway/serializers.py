from rest_framework import serializers
from .models import Job

class ReadJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['id', 'status', 'results', 'created_at', 'updated_at']

class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['document_content', 'document_metadata', 'pipeline_config']

    def validate_pipeline_config(self, value):
        valid_stages = {'extraction', 'analysis', 'enrichment'}
        if not isinstance(value, list) or len(value) == 0:
            raise serializers.ValidationError("pipeline_config debe ser una lista no vacía.")
        
        for stage in value:
            if stage not in valid_stages:
                raise serializers.ValidationError(f"Etapa inválida en el pipeline: {stage}. Opciones válidas: {valid_stages}")
        return value