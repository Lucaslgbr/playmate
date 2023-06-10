from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import CategoriaSerializer
from playmate.team_management.models import Categoria


class CategoriaViewset(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class=CategoriaSerializer
