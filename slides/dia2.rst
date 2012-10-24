==========================================
Django, el framework para perfeccionistas
==========================================

**Taller Intermedio**

:autor: Martín Gaitán
:evento: iSummit 2012
:lugar: Loja, Ecuador
:fecha: Miéroles 24 de octubre, 2012

|
|

.. image:: static/img/cc_by_sa-3.png


----

Quién
======

- Martín Gaitán
- Ingeniero en Computación - Universidad Nacional de Córdoba, Argentina
- Hincha de Boca Jr. (pero Fuerza Liga de Loja esta noche!)
- Python desde 2007, Django desde 2010
- Miembro de Python Argentina (python.org.ar)
- Creando Phasety (phasety.com) y trabajando en Machinalis (machinalis.com)

|
|    @tin_nqn_   \\   gaitan@gmail.com   \\   http://mgaitan.github.com

----

Qué
======

- Repaso de conceptos clave
- URLs
- Vistas
- Validación de formularios
- Vistas genéricas
- Tests
- South
- Ajax (?)

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

    - ``3 + 4.4, int(1j**2), 10 % 1``
    - Tambien existe ``decimal`` y en Django ``DecimalField``

- Listas

    - ``a = [4.0, 'Hola', Posicion()]``
    - ``a[1] == 'Hola'  # devuelve True``
    - ``range(-2, 4)``
    - ``[p.x for p in posiciones if p.y > 0]``

- Diccionarios:

    - ``hinchada = {'Martín': 'Boca Jr', 'Ramiro': 'Barcelona'}``
    - ``hinchada.keys() , hinchada['Maria'] = 'Liga de Loja'``


----

Repaso 2
===========

- Funciones

.. sourcecode:: python

    def potenciar(n, exp=2):
        return n**exp

- Tambien: ``potenciar = lambda n, exp: n**exp``

- Clases:

.. sourcecode:: python

    class MiModelo(models.Models):
        pass

- Tip: soporta multiherencia ``Hijo(Padre1, Padre2)``

Repaso 3
========

Control:

.. sourcecode:: python

    # iteracion
    for ticket in Tickets.object.all():
        print ticket.titulo

    # condicional
    if ticket.vencimiento >= datetime.now():
        alarma.sonar()


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


---

Hagamos *nuestras* paginas
==========================

**Vistas**

* Lógica de la aplicación
* Función normal
* Argumento: Request
* Valor de retorno: Response

----

Lo escencial
============

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

Pero hagamosló bien
=====================

- Vista listado (portada)

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


-----

.. sourcecode:: python

    >>> contact_form = ContactForm()
    >>> print contact_form.as_p()

    >>> mi_form.is_valid()  # no porque está vacío!
    >>> datos = {'asunto': 'Curso', 'remitente': 'gaitan@gmail.com',
                'mensaje': 'muy interesante'}
    >>> otro_form = ContactForm(datos)
    >>> otro_form.is_valid()     # si

----

Patrón típico
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

Lo mismo pero más pro
======================

.. sourcecode:: python

    def contacto(request):
       data = request.POST if request.method == "POST" else None
       form = ContactForm(data)
       if form.is_valid():
           # aqui usamos los datos validos
           return redirect(...)

        return render(request, "contact.html", {
                    "form": form,
                })

----

Validaciones propias
=====================

    clean()


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

Revisemos las vistas
=====================

- Buscar datos de la base (muchos, uno) y..

    - mostrarlos a traves de un template
    - editarlos con un formulario

- Suena bastante típico
- ¡No te repitas!

    class TicketDetailView(DetailView):
        model = Ticket

    class TicketListView(ListView):
        model = Ticket

    # paginar


# Context request

South
======

- Problema: migración de esquema




