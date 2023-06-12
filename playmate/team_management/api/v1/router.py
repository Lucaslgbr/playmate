from playmate.team_management.api.v1.viewsets import *

viewsets = [
    {'path':'categoria','viewset':CategoriaViewset},
    {'path':'cidade','viewset':CidadeViewset},
    {'path':'clube','viewset':ClubeViewset},
    {'path':'combinacao','viewset':CombinacaoViewset},
    {'path':'competicao','viewset':CompeticaoViewset},
    {'path':'equipe_atleta','viewset':EquipeAtletaViewset},
    {'path':'estado','viewset':EstadoViewset},
    {'path':'usuario','viewset':UsuarioViewset},
    {'path':'equipe','viewset':EquipeViewset},

]