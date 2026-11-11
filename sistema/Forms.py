from django.forms import forms
from sistema.models import *
 
# Checagem de email
# checagem de senha
# checagem de dado inserido



ESPECIALIDADES = [
        ('CARDIOLOGIA','Cardiologia')
        ('DEMARTOLOGIA', 'Dermatologia'),
        ('GINECOLOGIA', 'Ginecologia'),
        ('NEUROLOGIA','Neurologia'),
        ('OFTALMOLOGISTA','Oftalmologista'),
        ('ORTOPEDIA','Ortopedia'),
        ('PEDIATRIA','Pediatria'),
    ]

#Formulario do medico (para cadastro e edição)
class MedicoForm(forms.ModelForm):
    #Troca o charfield padrão por um select com opções fixas
    especialidades = forms.ChoiceField(
        choice=[('','Selecione uma especialidade')] + ESPECIALIDADES,
        label='eSPEIALIDADES',


    )

    class Meta:
        model = Medico
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'crm','especialidade']
        #criação_data e ativo não aparecem: são preenchidos automaticamente.
        labels = {
            'nome':'Nome',
            'sobrenome':'Sobrenome',
            'email':'E-mail',
            'telefone':'Telefone',
            'crm':'CRM',

        }


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

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['observacao','status']

        labels={
            'observacao':'Observacao',
            'status':'status',
        }
