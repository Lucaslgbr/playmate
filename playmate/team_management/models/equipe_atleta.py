from django.db import models
from playmate.team_management.models.usuario import Usuario
from playmate.team_management.models.equipe import Usuario
from playmate.team_management.enums.situacao_equipe_atleta import SituacaoEquipeAtleta

class EquipeAtleta(models.Model):
    equipe = models.ForeignKey('Equipe', on_delete=models.DO_NOTHING)
    atleta = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
    situacao = models.IntegerField(choices=SituacaoEquipeAtleta.choices)
    fixo = models.BooleanField(default=False)