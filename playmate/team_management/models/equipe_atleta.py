from django.db import models
from playmate.team_management.models.usuario import Usuario
from playmate.team_management.models.equipe import Usuario
from playmate.team_management.enums.situacao_equipe_atleta import SituacaoEquipeAtleta
from django.core.mail import send_mail
from playmate.settings import DEFAULT_FROM_EMAIL
class EquipeAtleta(models.Model):
    equipe = models.ForeignKey('Equipe', on_delete=models.DO_NOTHING)
    atleta = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
    situacao = models.IntegerField(choices=SituacaoEquipeAtleta.choices)
    fixo = models.BooleanField(default=False)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.situacao in [SituacaoEquipeAtleta.APROVADO, SituacaoEquipeAtleta.REJEITADO, SituacaoEquipeAtleta.CANCELADO]:
            if self.atleta.clube.tecnico.email:
                subject='Playmate | Status de aprovação em equipe'
                message = f'O status da solicitação do atleta {self.atleta} foi alterado para {self.get_situacao_display()}'
                send_mail(subject, message, DEFAULT_FROM_EMAIL, [self.atleta.clube.tecnico.email])


    def __str__(self) -> str:
        return f"{self.equipe}"