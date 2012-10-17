from django.shortcuts import render, redirect
from models import Proyecto, Ticket
from forms import TicketForm

def listar_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, "ticket_listar.html", {
                "tickets": tickets
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
