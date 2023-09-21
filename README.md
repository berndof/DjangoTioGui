
# Projeto CRUD django

 
- [ ] criar o ambiente virtual (venv)
- [ ] subpasta chamada src
- [ ] pip install django
- [ ] python hello_world 

***

```bash
mkdir src
django-admin startproject src .
cd src
python manage.py runserver
```

## django

#### fluxo do django

[django request workflow](https://nitinnain.com/djangos-request-response-cycle/)

#### principais configurações


#### principais comando django admin:

para usar o djangoadmin no projeto criado usamos o `manage.py`

- **createsuperuser** : adiciona usuario com permissão de staff (modelo padrão do django)
- **makemigrate**: cria o script para mudar o banco baseado nos modelos criados
- **migrate**: rodar depois do makemigrate para efetivar as mudanças no banco
- **runserver**: roda um servidor de testes
- **startapp {name}**: cria a estrutura de um app
- **startprojet {name} {path}**: cria a estrutura de um projeto


#### Apps
apps são como subprojetos, mais facil de trabalhar separadamente em cada um


#### Passos

- [ ] startar o projeto

- [ ] criar o app (core)

- [ ] adicionar a url para o app (core)
``` python

django urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')) #direciona a url / para o aninhamento de urls do core .urls
]
```

- [ ] criar o arquivo urls.py dentro do app (core)

- [ ] adicionar a primeira url (copiar a estrutura)

urlpatterns = [
    path('', home)
]

## Views


Criar um view dentro de core 

function based view 

def home (request)
    return render (request, index.html)
##

import a view no core.urls

from .view import home

function based view 

def home (request)
    return render (request, index.html)


runserver -> template does not exists

criar namespace
mkdir core/templates

touch index.html
fazer um hello, world

testar denovo 

instalar o app 
settings.py
INSTALLED_APPS
'core',

Começar com o crud

criar model dentro do core 

# models são estruturas de dados para o banco de dados

code/core/models.py

class Pessoa(models.Model):
    nome=models.CharField(max_length=100) #limite maximo de 100 caracteres

## registrar o model no admin

code/core/admin.py

# Register your models here.
from.models import Pessoa

admin.site.register(Pessoa)

#evoluir o banco de dados 
python manage.py makemigrations

#cria arquivo para criação das tabelas no banco de dados

agora migrar 
python manage.py migrate

# acessar o admin e ver se adicionamos uma "Pessoa"

definir o metodo __str__ da classe 

def __str__(self):
    return self.nome
            nome que aparece no admin

# voltar na view e importar o model

code core/views

from .models import Pessoa

dentro da view home 

pessoas = Pessoa.objects.all()

              /core/templates
#adicionar ao template index.html


                              {"nome da variavel": valor da variavel}
return request, "index.html", {"pessoas": pessoas}


agora temos o acesso a variavel dentro do template

utilizando jinja no html 

dentro do body do html 

abrir uma tag de lista <ul>

para cada "pessoa" da lista atribuir uma <li> (linha na lista)

dentro da tag <ul>

## {% para comandos %}  {{variaveis}}

{% for pessoa in pessoas %}
    <li> {{ pessoa.id }} - {{pessoa.nome}}
{% endfor %}


cRud
Read do crud concluido

## vamos fazer o create agora, cadastrar uma pessoa nova

adicionar um formulario no index.html do core 

<body>
    <form action="{% url 'salvar' %}" method="POST">
        <input type="text" name="nome">
        <button type="submit" >Salvar</button>
    </form>
</body>



cria um formulario que direciona para a view atrelada url que vamos criar 'salvar'
            direciona para url     enviar um post para a url
<form action="{% url 'salvar' %}" method="POST">

adiciona a tag input como texto e botão para enviar (type="submit")

importar a view salvar 

adicionar a url 
    endereço da url      view(proximo passo)  name para acessar pelo jinja como variavel
path("salvar/"         , salvar,               name=salvar)



criar a view salvar dentro do core em baixo da home 

def salvar(request)
    nome = request.POST.get("nome")
    Pessoa.objects.create(nome=nome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html, {"pessoas": pessoas})

o nome que eu dei no formulario, é como eu acesso a variavel no metodo post 
    nome = request.POST.get("nome")

    pego o valor inserido no request

## Crio um dado novo no banco 

Pessoa.objects.create(nome=nome)

com os atributos necessários para a crição do objeto

pessoas = Pessoa.objects.all()
envio a lista atualizada para o formulário


tentar = erro de CSRF (proteção de ataques cross-site do django)

[19/Sep/2023 22:44:04] "POST /core/salvar/ HTTP/1.1" 403 2506
Forbidden (CSRF token missing.): /core/salvar/

[Artigo](https://hackersec.com/o-que-e-csrf/)

precisa adicionar o token no formulário

dentro do <form> adicionar uma linha 

{% csrf_token %}

CRud
Create pronto

## Criar um campo para edição 

no core/index.html dentro do <li> adicionar a href

<li> {{pessoa.id}} - {{pessoa.nome}} <a href="{% url 'editar' pessoa.id %}">Editar</a>  </li>

## adicionar a url no core 

padrão diferente, url recebe variavel
                            view    variavel
path('editar/<int:id>',    editar, name="editar")
            recebe um id
            tipo inteiro

importar a view

# criar a view dentro do core

def editar(request, id) atributo|variavel
pessoa = Pessoa.objects.get(id=id) #procura a pessoa pela coluna id com a entrada da função
return render(request, "edit.html", {"pessoa": pessoa} )
                                    passo a variavel pro jinja

retornamos outro template, precisamos adicionar o html no templates

## template de edição 

    <h1>Editando:{{pessoa.id}} - {{pessoa.nome}}</h1>

                                enviando o id
    <form action="{% url 'update' pessoa.id %}" method="POST">
        {% csrf_token %}
        <input type="text" name="novo_nome">
        <button type="submit">Confirmar Edição</button>
    </form>

# criar a url "update" dentro de core/urls.py
path('update/<int:id>', update, name="update"),
            recebendo o id

importar a view update

# criar a view dentro do core/views.py

importar o redirect shortcuts

def update(request, id):
    novo_nome = request.POST.get("novo_nome")#coleto a variavel do formulario
    pessoa = Pessoa.objects.get(id=id) #acho a pessoa pelo id 
    pessoa.nome = novo_nome #mudo o nome
    pessoa.save() #salvo no banco 
    return redirect(home) #redirect(view)

## mesmo processo do edit para o delete, começar no index.html li/