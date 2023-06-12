from rest_framework import serializers

from playmate.team_management.models import Clube


class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clube
        fields='__all__'