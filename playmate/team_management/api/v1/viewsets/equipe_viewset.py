from rest_framework.viewsets import ModelViewSet
from playmate.team_management.api.v1.serializers import EquipeSerializer
from playmate.team_management.models import Equipe, EquipeAtleta
import json
from playmate.team_management.api.v1.viewsets.login_required_modelviewset import LoginRequiredModelViewSet

class EquipeViewset(LoginRequiredModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class=EquipeSerializer



    def filter_queryset(self, queryset):
        qs = super(EquipeViewset, self).filter_queryset(queryset)
        completed = self.request.query_params.get('completed')
        if completed != None:
            completed = json.loads(completed)
            equipes = []
            if completed:
                for equipe in Equipe.objects.all():
                    if EquipeAtleta.objects.filter(equipe=equipe).count() > 1:
                        equipes.append(equipe.id)
            else:
                for equipe in Equipe.objects.all():
                    if EquipeAtleta.objects.filter(equipe=equipe).count() < 2:
                        equipes.append(equipe.id)
                        print(completed, completed)
            return qs.filter(id__in=equipes)
        else:
            return qs