from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import CompeticaoSerializer
from playmate.team_management.models import Competicao


class CompeticaoViewset(ModelViewSet):
    queryset = Competicao.objects.all()
    serializer_class=CompeticaoSerializer
