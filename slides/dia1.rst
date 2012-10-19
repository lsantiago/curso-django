==========================================
Django, el framework para perfeccionistas
==========================================

- Taller Introductorio
 
- Atica iSummit 2012
 
-  `Creative Commons Atribución-CompartirIgual <http://creativecommons.org/licenses/by-sa/3.0/deed.es_AR>`_

.. image:: static/img/cc_by_sa-3.png


----

Quién
======

- Martín Gaitán
- Ingeniero en Computación - Universidad Nacional de Córdoba, Argentina
- Hincha de Boca Jr.
- Python desde 2007, Django desde 2010
- Creando Phasety (phasety.com) y trabajando en Machinalis (machinalis.com)
- Contactos: 
 
    @tin_nqn_ | gaitan@gmail.com | http://mgaitan.github.com

----
    
Qué
======

- Micro introduccion a Python
- Micro introducción a "la web"
- Introducción a Django
    
    - Ideas generales
    - Modelos
    - Vistas
    - Templates
    - URL
    - Tests

----

Cómo 
======

- Es un curso taller 
- En los talleres nos engrasamos las manos **¡Eso es muy bueno!**
    
    - Haremos una pequeña aplicación web con Django!

- Trabajamos en equipos ? 
- Pocos slides, más explicaciones. 
- Pueden preguntarme en cualquier momento / Puedo no saber responder de inmediato. 
    
.. warning::
    
    A veces hablo mucho. ;)
   

----   

Créditos
=========

Este material está basado en trabajos de 

- Santiago Piccinini
- Alejandro Peralta
- Daniel Moisset
- Ramiro Morales
    
Bajo licencias Creative Commons by-sa

    ** ¡Gracias! **

----

Empezamos ? 
============

A todo esto, ¿Qué es Python?
+++++++++++++++++++++++++++++

.. epigraph::
    
    El canónico *"Python es un gran primer lenguaje"* suscitó 
    *"¡Python es un gran último lenguaje!"*

    -- Noah Spurrier

----

En serio, qué es Python ?
===========================

.. image:: static/img/python-powered.png
   :align: right

* Un lenguaje de alto nivel

    * (muy) Fácil de aprender
    * con sintáxis legible y expresiva
    * Multiplataforma
    * Multiparadigma
    * Dinámico
    * Fuertemente tipado
    * Interpretado 
    * Interactivo
    * Extensible
    * Libre, Gratis y amigable comercialmente
    * Con las baterías incluídas
    * Con gran documentación 
    * y una maravillosa comunidad de usuarios

----

Quien lo usa
=============

.. epigraph::
    
    Si no me dedicara al fútbol programaría Python

    -- Lionel Messi
    
En serio
++++++++

    - Google
    - NASA
    - Yahoo
    - Mozilla
    - Las empresas donde trabajo
    - http://wiki.python.org/moin/OrganizationsUsingPython
    - Ustedes!

----

Para qué sirve Python
=======================

- Scripting general rápido
- Ingeniería
- Web
- Juegos
- Procesamiento de texto y lenguaje
- Interfaz entre distintos lenguajes
- Mucho mucho más...
- Y la combinación de todas ellas

----

Tan fácil de aprender?
========================

- Ejecutar la consola interactiva y hacer una suma::

    $ python
    Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.

- Pero mejor ``ipython`` ::
    
    $ ipython
    Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
    Type "copyright", "credits" or "license" for more information.

    IPython 0.13 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]:
    
----

A practicar!
=============
    
.. sourcecode:: python
    
    In [1]:  10 + 4
    Out[1]: 14
    
    In [2]: print 'Hola Loja!'
    Hola Loja!
    
---

Y ahora, un programa
=====================

- Abrir un editor (``gedit``, por ejemplo) y escribir una función

.. sourcecode:: python

    def alcuadrado(n):    
        res = n ** 2
        return res
    
    print alcuadrado(3)

- Guardarlo como ``cuadrado.py`` y ejecutarlo::

    $ python cuadrado.py
    
----

Más ? 
==========

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
            x = self.x**2 + self.y**2
            return math.sqrt(x)

-----

Y usamos
=========

.. sourcecode:: python

    >>> import posicion
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



