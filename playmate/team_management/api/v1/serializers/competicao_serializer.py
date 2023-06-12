from rest_framework import serializers

from playmate.team_management.models import Competicao


class CompeticaoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Competicao
        fields='__all__'