from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from models import Ticket, Proyecto

class TicketTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('juan', 'juan@midom.org',
                                             'passwd')
        proyecto = Proyecto.objects.create(nombre="Prueba",
                                           slug='prueba')
        self.simple_ticket_conf = {
            "titulo": "Bug de prueba",
            "descripcion": "Descripcion de un bug de prueba",
            "autor": self.user,
            "proyecto": proyecto
        }

    def test_basic_creation(self):
        ticket = Ticket.objects.create(**self.simple_ticket_conf)
        self.assertEqual(ticket.id, 1)
        self.assertEqual(unicode(ticket), u'#1: Bug de prueba')
        self.assertEqual(ticket.estado, "AB")

    def test_user_relation(self):
        ticket = Ticket.objects.create(**self.simple_ticket_conf)
        self.assertTrue(ticket in self.user.tickets_creados.all())
        self.assertFalse(ticket in self.user.tickets_asignados.all())

    def test_listar_tickets(self):
        response = self.client.get(reverse("ticket-listado"))
        self.assertEqual(response.status_code, 200)
