from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from playmate.team_management.enums import TipoUsuario
from playmate.team_management.enums import SexoUsuario

class Usuario(AbstractUser):
    data_nascimento = models.DateField(null=True, blank=True,)
    email = models.EmailField()
    tipo = models.IntegerField(choices=TipoUsuario.choices, default=TipoUsuario.ATLETA)
    clube = models.ForeignKey('Clube', null=True, blank=True, on_delete=models.DO_NOTHING)
    sexo = models.IntegerField(choices=SexoUsuario.choices, default=SexoUsuario.MASCULINO)
    observacao = models.CharField(max_length=500, null=True, blank=True)
    