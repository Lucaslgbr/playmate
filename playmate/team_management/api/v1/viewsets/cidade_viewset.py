from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import CidadeSerializer
from playmate.team_management.models import Cidade


class CidadeViewset(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class=CidadeSerializer
