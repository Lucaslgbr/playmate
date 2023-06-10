from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import ClubeSerializer
from playmate.team_management.models import Clube


class ClubeViewset(ModelViewSet):
    queryset = Clube.objects.all()
    serializer_class=ClubeSerializer
