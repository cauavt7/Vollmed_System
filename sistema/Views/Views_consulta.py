from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#pagina responsavel pela area medico
def consulta_view(request):
    print('Página funcionando')
    return HttpResponse('Página inicial das consultas')
