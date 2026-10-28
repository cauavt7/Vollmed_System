from django.db import models #orm do django para declarar modelos no banco de dados
from django.utils import timezone #Util para gerar data/hora atual no projeto.

#modelo que representa um Paciente.
#aributos => nome,sobrenome, email,telefone,data de cadastro,mensagem, ativo(true/False).
class Paciente(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    criacao_data = models.DateTimeField(default = timezone.now) #Data/Hora do cadastro
    Mensagem = models.TextField(blank=True) #campo opicional livre pre mensagem.
    ativo = models.BooleanField(default=True) #campo de exclusão logica 

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Medico(models.Model):
    nome =models.CharField(max_length=25)
    Sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=50)
    crm = models.CharField(max_length=6)
    criacao_data = models.DateTimeField(default = timezone.now)
    Mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome} {self.Sobrenome}'

class Consulta(models.Model):
    paciente_id = models.ForeignKey(Paciente,on_delete = models. CASCADE)
    medico_id =   models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_consulta = models.DateTimeField(default=timezone.now)
    ativa =  models.BooleanField(default=True) #campo de exclusão lógica
    observacao = models.TextField(blank=True)#anotação opcional
    status = models.CharField(
        default='A',
        max_length=1,
        choices=[
            ('A','Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada'),
        ]


        
    )

