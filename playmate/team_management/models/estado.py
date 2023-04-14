from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=255)