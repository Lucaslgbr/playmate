from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import EquipeSerializer
from playmate.team_management.models import Equipe, EquipeAtleta
import json

class EquipeViewset(ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class=EquipeSerializer



    def filter_queryset(self, queryset):
        qs = super(EquipeViewset, self).filter_queryset(queryset)
        completed = json.loads(self.request.query_params.get('completed', 'false') )
        print(completed)
        equipes = []
        if completed:
            print(completed, completed, completed)
            for equipe in Equipe.objects.all():
                if qs.filter(equipe=equipe).count() > 1:
                    equipes.append(equipe.id)
        else:
            for equipe in Equipe.objects.all():
                if qs.filter(equipe=equipe).count() < 2:
                    equipes.append(equipe.id)
                    print(completed, completed)
        return qs.filter(id__in=equipes)