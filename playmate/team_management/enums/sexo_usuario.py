from django.db import models


class SexoUsuario(models.IntegerChoices):
    MASCULINO = 1, 'MASCULINO'
    FEMININO = 2, 'FEMININO'
