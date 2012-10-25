# -*- coding: utf-8 -*-
from django import forms
from models import Ticket


class ContactForm(forms.Form):
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField()
    remitente = forms.EmailField()
    cc_a_mi = forms.BooleanField(required=False)


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
