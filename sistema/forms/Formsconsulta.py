from django.forms import forms
from sistema.models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['observacao','status']

        labels={
            'observacao':'Observacao',
            'status':'status',
        }



