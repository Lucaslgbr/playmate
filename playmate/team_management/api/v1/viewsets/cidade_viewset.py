from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import CidadeSerializer
from playmate.team_management.models import Cidade
from playmate.team_management.api.v1.viewsets.login_required_modelviewset import LoginRequiredModelViewSet


class CidadeViewset(LoginRequiredModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class=CidadeSerializer
