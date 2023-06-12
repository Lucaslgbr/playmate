from rest_framework import serializers

from playmate.team_management.models import Equipe


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipe
        fields='__all__'