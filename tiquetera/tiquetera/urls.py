from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        'tiquetera.tickets.views.listar_tickets',
        name='ticket-listado'),
    url(r'^ticket/(?P<id>\d+)/$',
        'tiquetera.tickets.views.detalle_ticket',
        name='ticket-detalle'),
    url(r'^ticket/(?P<id>\d+)/editar/$',
        'tiquetera.tickets.views.editar_ticket',
        name='ticket-editar'),
    url(r'^admin/', include(admin.site.urls)),
)
