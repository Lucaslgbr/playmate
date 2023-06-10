from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import CombinacaoSerializer
from playmate.team_management.models import Clube


class CombinacaoViewset(ModelViewSet):
    queryset = Clube.objects.all()
    serializer_class=CombinacaoSerializer
