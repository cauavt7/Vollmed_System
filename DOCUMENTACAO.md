# Comandos do django

1. ``pip instal django`` -> ele instala o django no projeto.
2. ``Django-admin startproject nome_do_projeto.`` -> Criando um novo projeto em django.
3. ``python manage.py runserver`` -> Subindo o servidor.
4. ``python menage.py startapp nome_do_app`` -> Criando um novo app
5. ``python manage.py migrate`` -> realiza as migrações(ativa) do projeto.
6. ``python manage.py createsuperuser`` -> Criar um novo usuário.
7. ``python manage.py changepassword`` nomedousuario -> Altera a senha, caso você esqueça.
8. ``python manage.py makemigrations`` -> Cria/gera um novo pacote de migração (util para novo app e alteração de BD)


# Tags do django html
> {%load static %} -> Habilit os static no arquivo . cada template que usa ``{%static%}`` precisa ser carregado.
> {%block title%} -> Insere o título da aba. As páginas filhas trocam.
> {%block header%} -> O header público (Logo+entrar). `O base_logado.html` troca por intero;
> {%block header actions%} -> Só o botão "entrar". O `login.html` esvazia o bloco.
> {%include ...%} -> insere as mensagens e/ou blocos de código.
> {% block content%} -> O miolo da pagína , cada filha vai ter seu própio <main>.

## TAGS DE ROTA
>{% url 'sistema:médico-list' %} -> Fica nos templates e se refere a uma lista de médicos que está no app sistema
>{%url 'sistema:médico-update' medico.pk%} -> Utilização ao template com parâmetro para update do médico.
>{%url url_voltar %} -> url_volta é o nome de uma variável que guada uma lógica de retorno a página anterior.
> Redirect('sistema:medico-list)-> fica nua view e informa que quando que quando uma ação fo realizado, o usuário será redirecionado.
GET
POST
PUT
DELETE
