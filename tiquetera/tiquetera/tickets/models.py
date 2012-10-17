# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

ESTADOS = (('AB', 'Abierto'), ('CE', 'Cerrado'),
           ('CU', 'En curso'))

class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)
    slug = models.SlugField()
    descripcion = models.TextField("descripción")

    def __unicode__(self):
        return self.nombre

class Ticket(models.Model):
    titulo = models.CharField("título", max_length=150)
    descripcion = models.TextField("descripción")
    proyecto = models.ForeignKey(Proyecto)
    autor = models.ForeignKey(User, related_name="tickets_creados")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    asignado_a = models.ForeignKey(User, null=True, blank=True,
                                   related_name="tickets_asignados")
    estado = models.CharField(max_length=2, choices=ESTADOS,
                              default="AB")

    def __unicode__(self):
        return u"#%d: %s" % (self.id, self.titulo)
