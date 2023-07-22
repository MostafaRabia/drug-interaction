from rest_framework import serializers
from .models import Drug, ActiveSubstance, Disease, ActiveSubstanceDisease

class DrugSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drug
        fields = ['url', 'name', 'active_substances']

class ActiveSubstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActiveSubstance
        fields = ['url', 'name', 'drugs', 'diseases']

class ActiveSubstanceDiseaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActiveSubstanceDisease
        fields = ['url', 'disease', 'active_substance', 'more_information']

class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disease
        fields = ['url', 'name', 'active_substances']
