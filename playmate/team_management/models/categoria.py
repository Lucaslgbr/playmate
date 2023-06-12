from django.db import models
from playmate.team_management.models.usuario import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    idade_minima = models.PositiveIntegerField()
    idade_maxima = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.nome} - de {self.idade_minima} a {self.idade_maxima} anos"