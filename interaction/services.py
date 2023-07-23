from models.models import Drug, Disease, ActiveSubstanceDisease
from django.shortcuts import get_object_or_404

class Interaction(object):

    @staticmethod
    def is_drug_interaction_disease(drug_id: int, disease_id: int) -> dict:
        interactions = ActiveSubstanceDisease.objects.filter(
            disease_id=disease_id,
            active_substance_id__in=get_object_or_404(Drug, pk=drug_id).active_substances.values_list('id')
        ).select_related('disease', 'active_substance').all()

        return_list = []

        for interaction in interactions:
            return_list.append({
                "disease": interaction.disease.name,
                "active_substance": interaction.active_substance.name,
                "more_information": interaction.more_information,
            })

        return {
            "is_safe": not return_list,
            "details": return_list
        }
