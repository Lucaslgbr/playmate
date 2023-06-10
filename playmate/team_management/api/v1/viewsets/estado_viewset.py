from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import EstadoSerializer
from playmate.team_management.models import Estado


class EstadoViewset(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class=EstadoSerializer
