from .URL_medicos import urlparttnes as medico_urlpatterns
from .URL_pacientes import urlparttnes as paciente_urlpatterns
from .URL_consulta import urlparttnes as consulta_urlpatterns

urlpatterns = medico_urlpatterns +paciente_urlpatterns +consulta_urlpatterns



    

