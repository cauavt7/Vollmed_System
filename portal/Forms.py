from django.forms import forms
from sistema.models import *

# Checagem de e-mail 
# Checagem de senha
# Checagem de dado inserido

class MedicoForm(forms.ModelForm):
    class Meta:
     model = Medico
     fields = ['nome''sobrenome'',email','telefone','crm','especialidade']


