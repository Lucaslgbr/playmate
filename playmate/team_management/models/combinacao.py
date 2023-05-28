from django.db import models
from playmate.team_management.enums.sexo_usuario import SexoUsuario

class Combinacao(models.Model):
    sexo = models.IntegerField(choices=SexoUsuario.choices)

    class Meta:
        verbose_name_plural = 'Combinações'
    