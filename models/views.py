from rest_framework import viewsets
# from rest_framework import permissions
from .models import Drug, ActiveSubstance, Disease, ActiveSubstanceDisease
from .serializers import DrugSerializer, ActiveSubstanceSerializer, DiseaseSerializer, ActiveSubstanceDiseaseSerializer

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

class ActiveSubstanceViewSet(viewsets.ModelViewSet):
    queryset = ActiveSubstance.objects.all()
    serializer_class = ActiveSubstanceSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class ActiveSubstanceDiseaseViewSet(viewsets.ModelViewSet):
    queryset = ActiveSubstanceDisease.objects.all()
    serializer_class = ActiveSubstanceDiseaseSerializer
