## login e autenticação
 conferir o

 "django.contrib.auth" no INSTALLED_APPS settings.py


incluir o app pronto de autenticação nas urls 

importar o include do django.urls
adicionar a url para o app do django

path('accounts/', include("django.contrib.auth.urls"))

[documentação](https://docs.djangoproject.com/en/4.2/topics/auth/default/)

The URLs provided by auth are:

accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']


criar os templates na raiz

mkdir 

src/templates/registration
touch src/templates/registration/login.html


<h2>Log In</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Log In</button>
</form>


verificar o settings.py para adicionar o path dos templates

'DIRS': [BASE_DIR / "templates"],

adicionar o redirecionamento de login

LOGIN_REDIRECT_URL = "/"

# criar um superuser

python manage.py createsuperuser

ja posso logar no login/ e no admin/

mas vai dar erro, criar a homepage

# criar os templates para logged in e logged out


templates/base.html
templates/home.html

base.html

<html>
<head>
  <meta charset="utf-8">
  <title>{% block title %}Django Auth Tutorial{% endblock %}</title>
</head>
<body>
  <main>
    {% block content %}
    {% endblock %}
  </main>
</body>

o home.html extende o arquivo base.html

<!-- templates/home.html -->
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
{% if user.is_authenticated %}
  Hi {{ user.username }}!
{% else %}
  <p>You are not logged in</p>
  <a href="{% url 'login' %}">Log In</a>
{% endif %}
{% endblock %}

href direcionando para a tela de login e a logica de logado ou não

fazemos tambem o update do login.html para extender o base.html

<!-- templates/registration/login.html -->
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
<h2>Log In</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Log In</button>
</form>
{% endblock %}

# adicionar a url da home
importar o TemplateView
from django.views.generic.base import TemplateView # new

path('', TemplateView.as_view(template_name='home.html'), name='home')

## talvez tenha problema com os templates, basta mudar o diretorio (tirar de registration?)


# criar logout link


adicionar o logout no home.html

{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
{% if user.is_authenticated %}
  Hi {{ user.username }}!
  <p><a href="{% url 'logout' %}">Log Out</a></p>
{% else %}
  <p>You are not logged in</p>
  <a href="{% url 'login' %}">Log In</a>
{% endif %}
{% endblock %}


Adicionar o redirect no settings.py
e atualizar o login

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
