from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import EquipeAtletaSerializer
from playmate.team_management.models import EquipeAtleta
from playmate.team_management.api.v1.viewsets.login_required_modelviewset import LoginRequiredModelViewSet


class EquipeAtletaViewset(LoginRequiredModelViewSet):
    queryset = EquipeAtleta.objects.all()
    serializer_class=EquipeAtletaSerializer
