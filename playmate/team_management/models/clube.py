from django.db import models
from playmate.team_management.models.usuario import Usuario

class Clube(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.ForeignKey('Cidade', on_delete=models.DO_NOTHING)
    estado = models.ForeignKey('Estado', on_delete=models.DO_NOTHING)
    tecnico = models.ForeignKey('Usuario', related_name='tecnico', on_delete=models.DO_NOTHING)
