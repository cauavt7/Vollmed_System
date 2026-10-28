from django.contrib import admin

from sistema import models

@admin.register(models.Paciente) # Registro o o paciente no portal do python
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email','telefone','ativo')

@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display =('id','nome','email','telefone','especialidade','crm','ativo')

@admin.register(models.Consulta)  
class ConsultaAdmin(admin.ModelAdmin): 
    list_display = ('paciente_id','medico_id','data_consulta','ativa','observacao','status')
     

