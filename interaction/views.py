from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import Interaction

@api_view(["get"])
def check_if_drug_interaction_disease(request):
    return Response(Interaction.is_drug_interaction_disease(request.query_params.get('drug'), request.query_params.get('disease')))
