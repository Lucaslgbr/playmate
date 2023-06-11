from django.db import models


class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.ForeignKey('Estado', on_delete=models.DO_NOTHING)
    

    def __str__(self) -> str:
        return self.nome