from rest_framework import serializers

from playmate.team_management.models import Cidade


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cidade
        fields='__all__'