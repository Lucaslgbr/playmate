from django.db import models


class SituacaoEquipeAtleta(models.IntegerChoices):
    APROVADO = 1, 'Aprovado'
    REJEITADO = 2, 'Rejeitado'
    SOLICITADO = 3, 'Solicitado'
    CANCELADO = 4, 'Cancelado'