from models.models import Drug, Disease
from django.shortcuts import get_object_or_404

class Interaction(object):

    @staticmethod
    def is_drug_interaction_disease(drug_id: int, disease_id: int) -> bool:
        drug = get_object_or_404(Drug, pk=drug_id)
        disease = get_object_or_404(Disease, pk=disease_id)

        return not set(drug.active_substances.values_list('id', flat=True)).isdisjoint(disease.active_substances.values_list('id', flat=True))
