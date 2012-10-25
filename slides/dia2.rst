==========================================
Django, el framework para perfeccionistas
==========================================

**Taller Intermedio/Avanzado**

:autor: Martín Gaitán
:evento: iSummit 2012
:lugar: Loja, Ecuador
:fecha: Miércoles 24 de octubre, 2012

|
|

.. image:: static/img/cc_by_sa-3.png


----

Quién
======

- Martín Gaitán
- Ingeniero en Computación - Universidad Nacional de Córdoba, Argentina
- Hincha de Boca Jr. (pero **Fuerza Liga de Loja esta noche!**)
- Python desde 2007, Django desde 2010
- Miembro de Python Argentina (python.org.ar)
- Creando Phasety (phasety.com) y trabajando en Machinalis (machinalis.com)

|
|    @tin_nqn_   \\\\   gaitan@gmail.com   \\\\   http://mgaitan.github.com

----

Qué
======

- Repaso de conceptos clave
- Vistas
- URLs
- Formularios y validación
- Vistas genéricas
- South

----

Cómo
======

- Seguiremos trabajando en *La Tiquetera*
- Experimento: pair programming.
- Más explicaciones y demos que diapositivas (esta vez será verdad)
- Pueden preguntarme en cualquier momento / Puedo no saber responder de inmediato.
  (esta vez es mucho más probable)

----

Repaso 1
==========

- Números:

.. sourcecode:: python

    >>> 3 + 4.4, int(1j**2), 10 % 1

- Tambien existe ``decimal`` y en Django ``DecimalField``

- Listas

.. sourcecode:: python

    >>> a = [4.0, 'Hola', Posicion()]
    >>> a[1] == 'Hola'
    True
    >>> range(-2, 3)
    [-2, -1, 0, 1, 2]
    >>> [p.x for p in posiciones if p.y > 0]

----

Repaso 2
=========

- Diccionarios:

.. sourcecode:: python

    >>> hinchada = {'Martín': 'Boca Jr',
                    'Ramiro': 'Barcelona',
                    'René': 'Barcelona'}
    >>> hinchada.values()       # keys()
    ['Boca Jr', 'Barcelona', 'Barcelona']

- Conjuntos:

.. sourcecode:: python

    >>> set(['Hola', 'Chau', 4, 'Chau'])
    set([4, 'Hola', 'Chau'])

----

Repaso 3
===========

- Funciones

.. sourcecode:: python

    def potenciar(n, exp=2):
        return n**exp

    # otra forma (inline)
    potenciar = lambda n, exp: n**exp

- Clases:

.. sourcecode:: python

    class MiModelo(models.Models):

- Soporta multiherencia

.. sourcecode:: python

    class Hijo(Padre1, Padre2):

-----

Repaso 4
========

Control:

.. sourcecode:: python

    # iteracion
    for ticket in Tickets.object.all():
        print ticket.titulo

    # condicional
    if ticket.vencimiento >= datetime.now():
        alarma.sonar()
    else:
        print "todo está bien, pelado!"


-----

Volvamos a Django
==================

|
|
|

.. image:: static/img/django.jpg
   :align: center

-----

Vimos
=======

- Proyecto vs. App: ``startproject`` ``startapp``
- Settings: conf base de datos y apps instaladas
- Crear nuestros modelos:

.. sourcecode:: python

    class Ticket(models.Model):
        titulo = models.CharField(max_length=150)
        descripcion = models.TextField()
        ...

- Creamos la base con ``manage.py syncdb``

----

Admin
=======

- Activamos en ``INSTALLED_APPS``
- Creamos nuestro ``admin.py``
- Declaramos ``url(r'^admin/', include(admin.site.urls)),``
- Usar!

- Pero recuerden: No es la bala de plata

----

Hagamos *nuestras* paginas
==========================

**Vistas**

* Lógica de la aplicación
* Función normal
* Argumento: Request
* Valor de retorno: Response

----

Un "Hola mundo"
================

.. sourcecode:: python

    #   views.py

    from django.http import HttpResponse

    def hola_mundo(request):
        return HttpResponse('Hola Mundo')

    # urls.py
    from django.conf.urls import patterns, url
    urlpatterns = patterns('',
        url(r'^hola-mundo$',
            'tiquetera.tickets.views.hola_mundo')
        )

- ``runserver`` e ir a http://localhost:8000/hola-mundo

----

Vista listado
==============

.. sourcecode:: python

    from django.shortcuts import render, redirect

    def listar_tickets(request):
        tickets = Ticket.objects.all()
        return render(request, "ticket_listar.html", {
                    "tickets": tickets
                })

- ``render`` es un atajo.
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


- Qué pasaría si id es un número de ticket que no existe?
- Otro shortcut: ``get_object_or_404(Ticket, id=id)``


----

Accediendo a las vistas: URLs
==============================

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

Template listado
=================

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

- Ver también ``ticket_detalle.html``

----

Algunos ``tags`` importantes
=============================

* ``{% block nombre_bloque %}``

        Porción *que puede redefinirse*

* ``{% extends 'template_base.html' %}``

        Herencia. Usar otro como base y redefinir bloques

* ``{% include 'pedacito.html' %}``

        Incrustar fragmentos desde otros templates

* ``{% url nombre_url parametro1, ... %}``

        Construir la url mediante su nombre. Igual a ``reverse()``

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


-----

Como funcionan?
===============

.. sourcecode:: python

    >>> contact_form = ContactForm()
    >>> print contact_form.as_p()    # as

    >>> mi_form.is_valid()  # no porque está vacío!
    >>> datos = {'asunto': 'Curso', 'remitente': 'gaitan@gmail.com',
                'mensaje': 'muy interesante'}
    >>> otro_form = ContactForm(datos)
    >>> otro_form.is_valid()     # si

----

En una vista
=============

.. sourcecode:: python

    def contacto(request):
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

-----

Opcional: como mandar emails ?
===============================

.. sourcecode:: python

    # en la vista
    from django.core.mail import send_mail

    send_mail('Asunto aqui',
             'cuerpo del mensaje',
             'remitente@ejemplo.com',
             ['para@ejemplo.com'], fail_silently=False)

    # Trampita: que envie el email a la pantalla.
    # en settings.py
    EMAIL_BACKEND = \
    'django.core.mail.backends.console.EmailBackend'

----

Lo mismo pero más pro
=========================

.. sourcecode:: python

    def contacto(request):
       data = request.POST if request.method == "POST" \
                           else None
       form = ContactForm(data)
       if form.is_valid():
           # aqui usamos los datos validos en send_mail
           return redirect(...)

       return render(request, "contact.html", {
                    "form": form,
                })


----

Validación
============

Además de las validaciones automáticas (dadas por el tipo de Field)
Django soporta validaciones y "limpiezas" propias.

- Pueden ser *por campo*
- O de todo el formulario (valiciones que dependen de multiples valores)

-------

Ejemplo
========

- Sólo correos de *@utpl.edu.ec* se pueden contactar.

.. sourcecode:: python

    class ContactForm(forms.Form):
        ...

        def clean_remitente(self):
            dato = self.cleaned_data['remitente']
            if not dato.endswith('utpl.edu.ec'):
                raise forms.ValidationError("Usa tu correo oficial")

        # acá podria manipular. pero siempre hay que devolver el dato
        return dato

-----

Otro ejemplo
==============

Si el mensaje no es de René, exigir que sea largo

.. sourcecode:: python


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        remitente = cleaned_data.get("remitente")
        mensaje = cleaned_data.get("mensaje")

        if (remitente != 'rrelizalde@utpl.edu.ec' and
             len(mensaje) < 50):
            raise forms.ValidationError(
                    "Su mensaje es demasiado breve" \
                    "y usted no es René.")
        # Siempre devolver el diccionario
        # de datos limpios
        return cleaned_data

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

-----

Y la vista editar
=================


.. sourcecode:: python

    def editar_ticket(request, id):
        ticket = Ticket.objects.get(id=id)
        if request.method == "POST":

          form = TicketForm(request.POST, instance=ticket)
          if form.is_valid():
              form.save()
              return redirect("ticket-detalle", id=id)
        else:
            form = TicketForm(instance=ticket)

        return render(request, "ticket_editar.html", {
                    "ticket": ticket,
                    "form": form,
                })

----

Vistas genéricas
================

- Buscar datos de la base (muchos, uno) y..

    - mostrarmos a traves de un template
    - editarlos con un formulario

- Suena bastante típico
- Recuerda: **¡No te repitas!**

-----

Vista listado en *generic views*
=================================

.. sourcecode:: python

    from django.views.generic import ListView

    class TicketListView(ListView):
        model = Ticket
        template_name = "ticket_listar.html"
        # template default: ticket_list.html
        context_object_name = "tickets"
        # default: object_list

    listar_tickets = TicketListView.as_view()

----

Detalles
========

- A diferencia de un vista común, las genéricas son clases.
- Para llamarlas desde una URL hay que usar ``as_view()``
- Para redefinir el *listado* (queryset) se define ``queryset`` o
  ``get_queryset()`` para filtrados dinámicos
- Paginacion gratis con ``paginate_by``

----

Ejercicios 1
=============

- Crear una vista que liste todos los tickets pertenecientes a un proyecto
- Usar el slug en la url. Ejemplo: ``/curso-django/``
- Tip: regex ``r'^(?P<slug>[-\w]+)$',``

- Crear una vista que liste todos los tickets asignados a un usuario
- Url ``r'^responsable/(?P<username>\w+)$'``

----

Ejercicios 2
==============

- Crear una vista que liste todos los tickets por estado:
- URL ``r'^estado/(?P<estado>[AB|CE|CU]$)'``

- Hacer un ``clean`` en el formulario que autoseleccione el
  User con id=1 si el proyecto tiene id=1.

------

South
======

- Problema: nuestro proyecto evoluciona
- Django crea tablas nuevas pero no altera existentes
- South: manejo de migraciones
- Ejemplo: queremos agregarle una fecha de vencimiento opcional
  a nuestro modelo ``Ticket``


----

South 2
========

- ``syncdb`` fallaría. Hay que usar South.

    - Lo instalamos (ejemplo: ``pip install south``)
    - Agregamos ``south`` a ``INSTALLED_APPS``
    - ``syncdb``
    - ``manage.py convert_to_south tickets``

------

Que sucedió?
=============

- Creó un archivo ``tickets/migrations/0001_initial.py``
- y *aplicó* esa migración
- Listo, ahora podemos hacer migraciones

----

South 3
========

- Modificamos nuestro modelo agregando el campo ``vencimiento``

.. sourcecode:: python

    class Ticket(models.Model):
        (...)
        vencimiento = models.DateField(null=True, blank=True)

- Creamos la migracion::

    $ manage.py schemamigration tickets --auto

- Crea una migracion ``0002_auto__add_field_ticket_vencimiento.py``
- La aplicamos::

    $ manage.py migrate tickets

----


Más ?
========

La documentación de Django es buenísima!

    * http://docs.djangoproject.com

Pueden consultarme

|
|    @tin_nqn_   \\   gaitan@gmail.com   \\   http://mgaitan.github.com

----

Y sumense a Python Argentina
============================

* http://www.python.org.ar
* Via IRC: #pyar en freenode.net

.. raw:: html

    <iframe width="560" height="315" src="http://www.youtube.com/embed/n899NT8JTSY" frameborder="0" allowfullscreen></iframe>


**Gracias por la participación!**



