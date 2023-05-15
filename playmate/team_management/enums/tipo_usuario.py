from django.db import models


class TipoUsuario(models.IntegerChoices):
    TECNICO = 1, 'TÉCNICO'
    ATLETA = 2, 'ATLETA'