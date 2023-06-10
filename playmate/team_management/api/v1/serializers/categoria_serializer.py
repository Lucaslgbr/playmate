from rest_framework import serializers

from playmate.team_management.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields='__all__'