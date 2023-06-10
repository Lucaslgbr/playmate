from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers.usuario_serializer import UsuarioSerializer
from playmate.team_management.models import Usuario
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class UsuarioViewset(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class=UsuarioSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = response.data.serializer.instance
        user.set_password(request.data['password'])
        user.save()
        return response