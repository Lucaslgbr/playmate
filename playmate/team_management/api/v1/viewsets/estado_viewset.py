from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import EstadoSerializer
from playmate.team_management.models import Estado
from playmate.team_management.api.v1.viewsets.login_required_modelviewset import LoginRequiredModelViewSet


class EstadoViewset(LoginRequiredModelViewSet):
    queryset = Estado.objects.all()
    serializer_class=EstadoSerializer
