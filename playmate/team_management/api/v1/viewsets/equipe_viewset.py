from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import EquipeSerializer
from playmate.team_management.models import Equipe


class EquipeViewset(ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class=EquipeSerializer
