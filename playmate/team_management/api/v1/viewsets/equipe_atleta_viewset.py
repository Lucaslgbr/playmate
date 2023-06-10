from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import EquipeAtletaSerializer
from playmate.team_management.models import EquipeAtleta


class EquipeAtletaViewset(ModelViewSet):
    queryset = EquipeAtleta.objects.all()
    serializer_class=EquipeAtletaSerializer
