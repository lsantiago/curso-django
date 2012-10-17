from django.contrib import admin
from models import Proyecto, Ticket

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}

class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha_creacion'
    list_display = ('__unicode__', 'autor', 'asignado_a',
                    'fecha_creacion', 'proyecto', 'estado' )
    list_display_links = ('proyecto', )
    list_editable = ('asignado_a', 'estado')
    list_filter = ('proyecto__nombre', 'estado')
    search_fields = ['id', 'titulo', 'descripcion']

admin.site.register(Proyecto, ProjectAdmin)

admin.site.register(Ticket, TicketAdmin)
