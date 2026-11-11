from django.forms import forms
from sistema.models import Medico
 



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
        label='ESPEIALIDADES',


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