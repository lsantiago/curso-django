==========================================
Django, el framework para perfeccionistas
==========================================

**Taller Introductorio**

:autor: Martín Gaitán
:evento: Atica / iSummit 2012
:lugar: Loja, Ecuador
:fecha: Lunes 22 de octubre, 2012

|
|

.. image:: static/img/cc_by_sa-3.png


----

Quién
======

- Martín Gaitán
- Ingeniero en Computación - Universidad Nacional de Córdoba, Argentina
- Hincha de Boca Jr.
- Python desde 2007, Django desde 2010
- Miembro de Python Argentina (python.org.ar)
- Creando Phasety (phasety.com) y trabajando en Machinalis (machinalis.com)

|
|    @tin_nqn_   \\\\   gaitan@gmail.com   \\\\   http://mgaitan.github.com

----

Qué
======

- Mini introduccion a Python
- Micro introducción a "la web"
- Introducción a Django

    - Ideas generales
    - Modelos
    - Admin
    - Vistas
    - URLs
    - Templates
    - Formularios

----

Cómo
======

- Es un taller
- En los talleres nos engrasamos las manos **¡Eso es muy bueno!**

  - Haremos un pequeño proyecto

- ¿Trabajamos en equipos ?
- Más explicaciones que diapositivas
- Pueden preguntarme en cualquier momento / Puedo no saber responder de inmediato.

----

Warning
===========

    A veces hablo mucho. :-/

----

Créditos
=========

Este material está basado en trabajos de

- Santiago Piccinini
- Alejandro Peralta
- Daniel Moisset
- Ramiro Morales

Bajo licencias Creative Commons by-sa

**¡Gracias!**

----

Agradecimiento Especial
========================

- A la UTPL, por la invitación
- A René Elilzalde y María del Carmen Cabrera,
  por todas las gestiones que hicieron para mi
  visita.

----

Empezamos ?
============

.. epigraph::

    El canónico *"Python es un gran primer lenguaje"* suscitó
    *"¡Python es un gran último lenguaje!"*

    -- Noah Spurrier

.. image:: static/img/python-powered.png
   :align: center
   :height: 244px
   :width: 165px

----

En serio, qué es Python ?
===========================

* Un lenguaje de muy alto nivel
* (muy) Fácil de aprender, con sintáxis legible y expresiva
* Multiplataforma, Multiparadigma (e Interactivo)
* Interpretado y Dinámico (pero fuertemente tipado)
* Extensible
* Libre, Gratis y amigable comercialmente
* Con las baterías incluídas (y grandes aplicaciones)
* Con gran documentación
* y una maravillosa comunidad de usuarios (

----

Quién lo usa
=============

.. epigraph::

    Si no me dedicara al fútbol programaría Python

    -- Lionel Messi

.. image:: static/img/messi-ok.jpg
   :scale: 70%

----

En serio
========

- Google
- NASA
- Mozilla
- Las empresas donde trabajo
- ¡Ustedes luego de este evento!

----

Para qué sirve Python
=======================

- Scripting general rápido
- Ingeniería
- Web
- Juegos
- Procesamiento de texto y lenguaje
- Interfaz entre distintos lenguajes
- Mucho, mucho más...
- Y la combinación de todas ellas

----

¿Tan fácil de aprender?
========================

Contestemos esa pregunta!

- Ejecutar la consola interactiva

.. sourcecode:: python

    $ python
    Python 2.7.3 (default, Aug  1 2012, 05:14:39)
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

----

Pero mejor ``ipython``
======================

.. sourcecode:: bash

    $ ipython
    Python 2.7.3 (default, Aug  1 2012, 05:14:39)
    Type "copyright", "credits" or "license" for more information.

    IPython 0.13 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]:

- Nuestros aliados: ``<tab>`` y ``?``

----

¡A practicar!
=============

.. sourcecode:: python

    In [1]: 10 + 4
    Out[1]: 14

    In [2]: saludo = 'Ubyn Ybwn!'

    In [3]: print saludo.decode('rot13') # que sucede?

    In [4]: import this   # y esto?

----

Dijimos **muy** alto nivel
===========================

Python trae potentes estructuras de datos *built-in*

    * Listas: contenedor ordenado de objectos
    * Tuplas: simil a listas pero *inmutables*
    * Diccionarios: mapas clave-valor
    * Conjuntos: objetos unicos, no ordenado
    * y más!

-----

Listas
=======

.. sourcecode:: python

    >>> a = [100, 'huevos', 'sal']
    >>> a
    [100, 'huevos', 'sal']
    >>> a[0]
    100
    >>> a[-2:]
    ['huevos', 'sal']
    >>> a + ['oro', 9]
    [100, 'huevos', 'sal', 'oro', 9]
    >>> a[0] = "manteca"
    >>> a
    ['manteca', 'huevos', 'sal']

----

Diccionarios
============

.. sourcecode:: python

    >>> dias = {"Ene": 31, "Jul": 30}
    >>> dias
    {'Ene': 31, 'Jul': 30}
    >>> dias["Ene"]
    31
    >>> dias["Ago"] = 31
    >>> dias["Jul"] = 31
    >>> dias
    {'Ago': 31, 'Ene': 31, 'Jul': 31}
    >>> "Mar" in dias
    False
    >>> dias.keys()
    (['Ago', 'Ene', 'Jul']
    >>> dias.values()
    [31, 31, 31])

----

Conjuntos
=========

.. sourcecode:: python

    >>> conjunto = {'Loja', 3, 3 }
    >>> conjunto
    set([3, 'Loja'])

    >>> 'Loja' in conjunto
    True

    >>> conjunto.intersection({3})
    set([3])

    >>> conjunto.difference({3})
    set(['Loja'])


Bucles
=======

- No hacen falta índices

.. sourcecode:: python

    >>> bichos = ["pulgas", "piojos"]
    >>> for bich in bichos:
    ...     print "Mata-" + bich
    ...
    Mata-pulgas
    Mata-piojos


----

If
===

.. sourcecode:: python

    if <expresion>:
        <suite>
    elif <expresion>:
        <suite>
    else:
        <suite>

- ``<expresion>`` evalúa a verdadero o falso
- ``<suite>`` un bloque de código (con la misma sangría)
- operadores: ``or``, ``and``, ``not``
- comparadores: ``< > == != in is``

----

Y ahora, un programa
=====================

Abrir un editor (``gedit``, por ejemplo) y escribir una **función**

.. sourcecode:: python

    def alcuadrado(n):
        res = n ** 2
        return res

    print alcuadrado(3)

Guardarlo como ``cuadrado.py`` y ejecutarlo::

    $ python cuadrado.py

----

Puede haber valores por *default*
=================================

.. sourcecode:: python

    def potenciar(n, exp=2):
        res = n ** exp
        return res

    >>> potenciar(2, 3)
    8

    def oracion(quien, que="corre", como="lento"):
        return "%s %s %s" % (quien, que, como)

    >>> oracion("El conejo", como="veloz")
    'El conejo corre veloz'

----

Cosas *pythonicas*
===================

- Desempaquetado y multiasignación

.. sourcecode:: python

    >>> elemento1, elemento2 = dos_elementos = ('Hola', 5)
    >>> dos_elementos
    ('Hola', 5)

    >>> elemento2
    5

- Listas por comprensión

.. sourcecode:: python

    >>> [num**2 for num in range(10) if num % 2 == 0]
    [0, 4, 16, 36, 64]

----

Espacios de nombre
===================

Python es modular y tiene *espacios de nombre*

    * Un ``.py`` es un módulo.
    * Un directorio con ``__init__.py`` es un paquete

.. sourcecode:: python

    >>> from cuadrado import alcuadrado
    >>> alcuadrado(1j)
    (-1+0j)

-----

Clases
=======

.. sourcecode:: python

    # posicion.py

    import math     # baterias incluídas!

    class Posicion(object):

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def distancia(self):
            """La hipotenusa.
               Pitágoras programaba Python"""
            x = self.x**2 + self.y**2
            return math.sqrt(x)

-----

Y usamos
=========

.. sourcecode:: python

    >>> import posicion    # importa todo el módulo
    >>> p1 = posicion.Posicion(3, 4)
    >>> p1.x
    3
    >>> p1.dist()
    5.0
    >>> p2 = posicion.Posicion(7, 9)
    >>> p2.y
    9
    >>> p1.y
    4

----

Herencia
=========

.. sourcecode:: python

    class PosicionRect(Posicion):
        """ Sistema sin diagonales """

        def distancia(self):
            return float(self.x + self.y)

    >>> p1 = PosicionRect(3, 4)
    >>> p1.dist()
    7.0

----

Métodos *mágicos*
===================

- Empiezan y terminan con ``__`` (doble *underscore*)
- Se usan indirectamente con operadores

.. sourcecode:: python

    class Posicion(object):
        ...

        def __unicode__(self):
            return u'(%.2f, %.2f)" % (self.x, self.y)


    >>> print p1
    u'(3.00, 4.00)'

----

Ya sabemos suficiente!
======================

Vayamos a la web!


----

A dónde?
=========

- La web usa el protocolo ``HTTP``
- Peticiones y respuestas...
- Entre un cliente y un servidor

.. image:: static/img/img_HTTP_request.png
   :align: center

----

Peticiones (*requests*)
========================

Mediante métodos, cabecera y parámetros (datos). Importantes:

- ``GET`` (pedir)
- ``POST`` (modificar)

- En general cuando uno *entra* a una página hace ``GET`` y cuando
  envia un formulario hace ``POST``.

----

Respuestas (*responses*)
===========================

- Código, Cabecera y Datos

    ``200 OK``, ``404 Not Found``

- Hypertext Transfer? Ahora es cualquier cosa!

  * html, json, fotos, videos de goles de Boca, etc.

----

Entonces: Django!
=================

|
|
|

.. image:: static/img/django.jpg
   :align: center

-----

Claves
=======

.. image:: static/img/legos.jpg
   :align: right

* Framework
* DRY
* MVC
* Licencia BSD
* Excelente documentación
* Baterías incluídas !

----

MVT (MCV)
=========

**Modelos**

    Definición y manejo de los datos. (Crear, Modificar, Guardar, etc)

**Vistas**

    Lógica de la aplicación. Reacciona con HTTP

**Templates**

    Visualización de la información

----

¿Qué hay en las baterías?
=========================

- Interacción con base de datos relacionales
- Abstracción ORM
- Interfaz ABM (*CRUD*) automática
- Testing
- Usuarios y autenticación
- Manejo de formularios
- Paginación
- Seguridad (CSRF, XSS, etc)
- Muchas otras cosas resueltas!

----

¡Engrasemosnos las manos!
=========================

- Objetivo: un sitio para manejar tickets (*bugs*, por ejemplo)
- Lo llamaremos

    **"La Tiquetera"**

- Descargar: ``tiquetera.zip`` desde http://bit.ly/tiquetera

----

Comenzar un proyecto
====================

¿A Qué llama Django un Proyecto?

    Conjunto de aplicaciones y configuraciones para un sitio en particular

.. sourcecode:: bash

    $ django-admin.py startproject tiquetera

.. image:: static/img/project.png
   :align: center

-----

Con una aplicación
==================

Y qué es una Aplicación ?

    - Una aplicación web que hace una tarea en particular (*weblog*, *encuesta*, etc)
    - Un proyecto puede tener muchas *apps*.
    - Una aplicación puede ser parte de distintos proyectos (son *pluggables*)

    - Hay muchisimas apps listas para usar! djangopackages.com

-----

.. sourcecode:: bash

    $ cd tiquetera
    $ django-admin.py startproject tiquetera

.. image:: static/img/app.png
   :align: center



----

Algunos comandos
================

``django-admin.py`` y ``manage.py``:

* ``startproject``
* ``startapp``
* ``runserver``: servidor de desarrollo
* ``shell``
* ``test``
* ``syncdb``: crea tablas según modelos
* ``dumpdata`` y ``loaddata``
* ``inspectdb`` para bases de datos existentes

``./manage.py help [comando]``

----

Settings
========

El archivo ``settings.py``:

* Contiene la configuración del proyecto
    * conf de base de datos
    * Idioma
    * ``STATIC_URL`` y ``STATIC_ROOT``
    * aplicaciones instaladas
    * etc.

----

El nuestro
==========

.. sourcecode:: python

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
        ...

    INSTALLED_APPS = (
        ...
        'django.contrib.admin',
        'tiquetera.tickets',)

----

Volvamos a la tiquetera
========================

**Requerimientos**

- Un ticket tiene un **id**, un **estado**, una **fecha**, un
  **título** y **descripción** y posiblemente un **responsable**
- Queremos ver listados de tickets, su detalle, cargar nuevos,
  cambiarles el estado, asignarles responsable, etc.

----

Modelando
==========

.. sourcecode:: python

    # models.py
    from django.db import models
    from django.contrib.auth.models import User

    ESTADOS = (('AB', 'Abierto'), ('CE', 'Cerrado'),
               ('CU', 'En curso'))

    class Ticket(models.Model):
        titulo = models.CharField(max_length=150)
        descripcion = models.TextField()
        autor = models.ForeignKey(User)
        fecha_creacion = models.DateTime(auto_now_add=True)
        asignado_a = models.ForeignKey(User, null=True,
                              blank=True)
        estado = models.CharField(max_length=2, choices=ESTADOS)

----

Construyamos la base
=====================

    $ python manage.py syncdb

----

¡Magia ORM!
===========

.. sourcecode:: sql

    $ python manage.py sqlall tickets
    BEGIN;
    CREATE TABLE "tickets_ticket" (
     "id" integer NOT NULL PRIMARY KEY,
     "titulo" varchar(150) NOT NULL,
     "descripcion" text NOT NULL,
     "autor_id" integer NOT NULL REFERENCES "auth_user" ("id"),
     "fecha_creacion" datetime NOT NULL,
     "asignado_a_id" integer REFERENCES "auth_user" ("id"),
     "estado" varchar(2) NOT NULL
    )
    ;
    CREATE INDEX "tickets_ticket_32ec34e8" ON "tickets_ticket" ("autor_id");
    CREATE INDEX "tickets_ticket_4a1d037a" ON "tickets_ticket" ("asignado_a_id");
    COMMIT;

----

Usando nuestros modelos interactivamente
=========================================

.. sourcecode:: bash

    $ python manage.py shell

.. sourcecode:: python

    >>> from tiquetera.tickets.models import Ticket
    >>> from django.contrib.auth.models import User
    >>> usuario = User.objects.all()[0]
    >>> Ticket.objects.all()
    []

----

    >>> Ticket.objects.create(
            titulo='Un bug',
            descripcion='Bug de prueba',
            autor=usuario, estado='AB')

    >>> Ticket.objects.filter(autor=usuario)
    [ticket]
    >>> t = Ticket.objects.filter(titulo__contains='bug')[0]
    >>> t.titulo
    'Un bug'

----

Usemos  Admin
===============

Interfaz ABM (CRUD)

* Gratis
* Muy configurable
* Fácil de extender
* ¡Pero no es la bala de plata!

----

Admin (cont)
============

.. sourcecode:: python

    # admin.py
    import models
    from django.contrib import admin

    class TicketAdmin(admin.ModelAdmin):
        date_hierarchy = 'fecha_creacion'
        list_display = ('__unicode__', 'autor',
                        'asignado_a', 'fecha_creacion',
                        'proyecto', 'estado' )
        list_display_links = ('proyecto', )
        list_editable = ('asignado_a', 'estado')
        list_filter = ('proyecto__nombre', 'estado')
        search_fields = ['id', 'titulo', 'descripcion']

    admin.site.register(Ticket, TicketAdmin)

----

Arrancamos el servidor de pruebas
=================================

.. sourcecode:: bash

    $ python manage.py runserver

- Y vamos en el navegador a

  http://localhost:8000/admin


----

Hagamos *nuestras* paginas
==========================

**Vistas**

* Lógica de la aplicación
* Función normal
* Argumento: Request
* Valor de retorno: Response

----

Vista Listado
==============

.. sourcecode:: python

    def listar_tickets(request):
        tickets = Ticket.objects.all()
        return render(request, "ticket_listar.html", {
                    "tickets": tickets
                })

- ``render()`` es un "shortcut".
- Crea un *response* llenando un *template* con datos de *contexto*

----

Vista Detalle
==============

.. sourcecode:: python

    def detalle_ticket(request, id):
        ticket = Ticket.objects.get(id=id)
        return render(request, "ticket_detalle.html", {
                    "ticket": ticket
                })

----

Accediendo a una vista: URLs
============================

``urls.py`` relaciona *direcciones* con vistas

* URLs limpias
* Cualquier tipo de diseño
* Basadas en *expresiones regulares*
* Desacopladas

----

Por ejemplo
===========

.. sourcecode:: python

    urlpatterns = patterns('',
        url(r'^$',
            'tiquetera.tickets.views.listar_tickets',
            name='ticket-listado'),
        url(r'^ticket/(?P<id>\d+)/$',
            'tiquetera.tickets.views.detalle_ticket',
            name='ticket-detalle'),
        url(r'^admin/', include(admin.site.urls)),
    )

- ``(?P<id>\d+)`` es una *regex* que filtra sólo digitos
- ``/ticket/1/`` invocará a ``detalle_ticket(request, id=1)``

----

Templates
=========

* Balance entre poder y simplicidad
* Pensado para diseñadores
* Las variables vienen en el contexto que envió la vista
* ``{{ obj }} {{ obj.key }} {{ obj.atributo }} {{ obj.metodo }}``
* Tags: lógica simple ``{%  %}``
* Filtros: alteraciones  ``{{ X|filtro }}``

----

Ejemplo
========

.. sourcecode:: django

    <h1>Listado de Tickets</h1>

    <ul>
    {% for ticket in lista_tickets %}
    <li>
      <a href="{{ ticket.get_absolute_url }}">
        {{ ticket.title|upper }}
      </a>
    </li>
    <p>{{ ticket.descripcion|truncatewords:"15" }}</p>
    {% endfor %}
    </ul>

----

Algunos ``tags`` importantes
=============================

* ``{% block nombre_bloque %}``

        Porción *que puede redefinirse*

* ``{% extends 'template_base.html' %}``

        Herencia

* ``{% include 'pedacito.html' %}``

        Incrustar fragmentos

----

Formularios
===========

- Django construye y valida formularios

.. sourcecode:: python

    from django import forms

    class ContactForm(forms.Form):
        asunto = forms.CharField(max_length=100)
        mensaje = forms.CharField()
        remitente = forms.EmailField()
        cc_a_mi = forms.BooleanField(required=False)

    >>> mi_form = ContactForm()
    >>> mi_form.as_p()
    >>> mi_form.is_valid()  # no porque está vacío!
    >>>

----

Patrón típico
=============

.. sourcecode:: python

    if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():

           # aqui usamos los datos validos
           # que están en form.cleaned_data
           # Ejemplo: mandamos el email

           return redirect(...)
    else:
        form = ContactForm()

    return render(request, "contact.html", {
                "form": form,
            })

----

Formularios para nuestros modelos
==================================

- Ya definimos el modelo
- Quiero un formulario que lo represente (para crear o editar)
- ¡No te repitas!

.. sourcecode:: python

    from django import forms
    from models import Ticket

    class TicketForm(forms.ModelForm):
        class Meta:
            model = Ticket

----

Más ?
========

**¡Nos vemos el miércoles!**






