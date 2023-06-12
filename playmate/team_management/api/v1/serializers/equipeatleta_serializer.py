from rest_framework import serializers

from playmate.team_management.models import EquipeAtleta


class EquipeAtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model=EquipeAtleta
        fields='__all__'