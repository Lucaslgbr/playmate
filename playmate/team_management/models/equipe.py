from django.db import models
from playmate.team_management.models.usuario import Usuario

class Equipe(models.Model):
    competicao = models.ForeignKey('Competicao', on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey('Categoria', on_delete=models.DO_NOTHING)
    tecnico = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)


    def __str__(self) -> str:
        return f"Técnico {self.tecnico} - Categoria {self.categoria}"