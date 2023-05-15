from django.db import models

class Competicao(models.Model):
    nome = models.CharField(max_length=255)
    data_final_inscricao = models.DateField()
    data_competicao = models.DateField()

