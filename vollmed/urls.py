"""
URL configuration for vollmed project.

The `urlpatterns` list routes URLs to views. For more information please see:
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Views-> Retornam algo, são funções , request -> response

from django.contrib import admin
from django.urls import path ,include
import sistema.urls



#Views-> Retornam algo, são funções , request -> response
#View responsavel pela tela inicial do medico


#view responsavel pela home

urlpatterns = [
    path('admin/', admin.site.urls),
   path('',include(sistema.urls)),# preciso chamar uma url do app sistema
    #path('',include(sistema.Views.py)),
]

#MVT(Models,views,templates)   
# (MVC)

#www.vollmed.online/
#www.vollmed.online/login
#www.vollmed.online/  --Voltei pra home /Logado


#MEDICO
#www.vollmed.online/
#www.vollmed.online/medico
#www.vollmed.online/medico/id  -> depois da verificaçaão pra saber que é medico
#www.vollmed.online/medico/id/alterar -> alterar cadastro do medico

#www.vollmed.online/medico/id/consultas

#PACIENTE
#www.vollmed.online/
#www.vollmed.online/paciente/id  -> perfil do pacinte
#www.vollmed.online/paciente/id/alterar -> alterar cadastro do paciente

#www.vollmed.online/paciente/id/consultas/cadastrar/
#www.vollmed.online/paciente/id/consultas/id/ -> ver,alterar,deletar

#SECRETARIO/SUPERUSER
#www.vollmed.online/paciente/id  -> perfil do secretario
#www.vollmed.online/paciente/id/alterar -> alterar cadastro do secretario

#www.vollmed.online/paciente/id/consultas/cadastrar/
#www.vollmed.online/paciente/id/consultas/id/ -> ver,alterar,deletar


#CONSULTA


