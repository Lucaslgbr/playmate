from rest_framework import serializers

from playmate.team_management.models import Estado


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estado
        fields='__all__'