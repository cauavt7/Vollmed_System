from django.urls import path
from sistema.Views import medico_view

urlparttnes = [

  path('medico/', medico_view),# vollmed.com/medico
   path('medico/novo'),
   path('medico/perfil<int: paciente_id>'),
   path('medico/listagem'),
  
]
