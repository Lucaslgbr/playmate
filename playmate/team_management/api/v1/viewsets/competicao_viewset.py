from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import CompeticaoSerializer
from playmate.team_management.models import Competicao
from playmate.team_management.api.v1.viewsets.login_required_modelviewset import LoginRequiredModelViewSet


class CompeticaoViewset(LoginRequiredModelViewSet):
    queryset = Competicao.objects.all()
    serializer_class=CompeticaoSerializer
