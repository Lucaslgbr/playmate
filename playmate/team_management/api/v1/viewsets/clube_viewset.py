from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import ClubeSerializer
from playmate.team_management.models import Clube
from playmate.team_management.api.v1.viewsets.login_required_modelviewset import LoginRequiredModelViewSet


class ClubeViewset(LoginRequiredModelViewSet):
    queryset = Clube.objects.all()
    serializer_class=ClubeSerializer
