from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import CategoriaSerializer
from playmate.team_management.models import Categoria
from playmate.team_management.api.v1.viewsets.login_required_modelviewset import LoginRequiredModelViewSet

class CategoriaViewset(LoginRequiredModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class=CategoriaSerializer
