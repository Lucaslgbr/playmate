from rest_framework import serializers

from playmate.team_management.models import Combinacao


class CombinacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Combinacao
        fields='__all__'