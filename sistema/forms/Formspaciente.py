from django.forms import forms
from sistema.models import Paciente


class PacienteForm(forms.ModelForm):
 class Meta:
        model = Paciente
        fields = ['nome','soberenome','email','telefone','cpf',]
        labels ={

        'nome':'Nome',
        'sobrenome':'Sobrenome',
        'email':'E-mail',
        'telefone':'Telefone',
        'cpf':'CPF'
        }