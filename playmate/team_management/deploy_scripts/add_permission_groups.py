from playmate.team_management.models import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

def run():
     for permission in [
        Permission.objects.get(codename='view_competicao'),
        Permission.objects.get(codename='change_competicao'),
        Permission.objects.get(codename='add_competicao'),
        Permission.objects.get(codename='view_equipeatleta'),
        Permission.objects.get(codename='change_equipeatleta'),
        Permission.objects.get(codename='add_equipeatleta'),
        Permission.objects.get(codename='view_equipe'),
        Permission.objects.get(codename='change_equipe'),
        Permission.objects.get(codename='add_equipe'),
        Permission.objects.get(codename='view_categoria'),
        Permission.objects.get(codename='change_categoria'),
        Permission.objects.get(codename='add_categoria'),
        ]:
            Group.objects.get_or_create(name='Técnico')[0].permissions.add(permission)

