from django.contrib import admin


import json
from playmate.team_management.models import *
admin.site.register(Categoria)
admin.site.register(Clube)
admin.site.register(Combinacao)
admin.site.register(Competicao)
admin.site.register(EquipeAtleta)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Usuario)



class EquipeDisponivelFilter(admin.SimpleListFilter):
    title='Equipes Completas'
    parameter_name='completa'
    
    def lookups(self, request, model_admin):
        return [
            ['true','Completas'],
            ['false','Incompletas'],
        ]
        
    def queryset(self, request, queryset):
        if self.value():
            completa = json.loads(self.value())
            equipes = []
            if completa:
                for equipe in Equipe.objects.all():
                    if EquipeAtleta.objects.filter(equipe=equipe).count() > 1:
                        equipes.append(equipe.id)
            else:
                for equipe in Equipe.objects.all():
                    if EquipeAtleta.objects.filter(equipe=equipe).count() < 2:
                        equipes.append(equipe.id)
            return queryset.filter(id__in=equipes)
        return queryset
    
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['competicao', 'categoria', 'tecnico']
    list_filter = ['competicao', 'categoria', 'tecnico', EquipeDisponivelFilter]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter()
        return queryset

admin.site.register(Equipe, EquipeAdmin)


