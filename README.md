# DjangoTioGui
 vamo caralho

mkdir src
django-admin startproject app src

cd src

python manage.py runserver

python manage.py migrate # popula o banco de dados

manage.py --help 

createsuperuser

localhost/admin

cria um app (pequena parte do sistema)
manage.py startapp core 

urls principais

django urls import include
url core/ include core.urls

touch core/urls.py
urls do core aninhadas  (
                            /core/adsda
                            /core/lbalblas
                        )

core.urls

urlpatterns = [
    path('', home)
]


django request [workflow](https://nitinnain.com/djangos-request-response-cycle/)

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

