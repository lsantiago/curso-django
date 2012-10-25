from django.shortcuts import render, redirect
from models import Proyecto, Ticket
from forms import TicketForm, ContactForm
from django.http import HttpResponse
from django.views.generic import ListView


def listar_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, "ticket_listar.html", {
                "tickets": tickets
            })

"""
class TicketListView(ListView):
    model = Ticket
    template_name = "ticket_listar.html"

listar_tickets = TicketListView.as_view()
"""

def contact(request):
    if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():

           print form.cleaned_data

           return redirect('/')
    else:
        form = ContactForm()

    return render(request, "contacto.html", {
                "form": form,
            })


def detalle_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, "ticket_detalle.html", {
                "ticket": ticket
            })

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
