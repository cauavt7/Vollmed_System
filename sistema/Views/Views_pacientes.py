from django.shortcuts import render
from sistema.models import Paciente
#from django.http import HttpResponse

# Create your views here.

#pagina responsavel pela area medico
def  index(request):
     return render(
        request,
        'global/base.html'
        )






#view responsavel por listar todos os pacientes
def listaPaciente(request):
     pacientes =  Paciente.objects.all() #-> [obj1,obj2,obj3]

     context = {
          'paciente':pacientes,
     }

     return render(
          request,
          'paciente/listar.html',
          context,
          )
           
     















#GLOBAL -> uma pagina inteira
#PARTIALS -> Uma parte da página (header,footer,formulário)

#SPA

#MVT -> template/base.html
