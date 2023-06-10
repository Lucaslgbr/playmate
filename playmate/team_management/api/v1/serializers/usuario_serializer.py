from rest_framework import serializers

from playmate.team_management.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields='__all__'