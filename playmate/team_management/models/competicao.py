from django.db import models

class Competicao(models.Model):
    nome = models.CharField(max_length=255)
    data_final_inscricao = models.DateField()
    data_competicao = models.DateField()

    class Meta:
        verbose_name_plural = 'Competições'
    
    def __str__(self) -> str:
        return f"{self.nome}"