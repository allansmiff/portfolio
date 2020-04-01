# -*- coding:utf-8 -*-
from django import forms
from localflavor.br.br_states import STATE_CHOICES


class FormContact(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField(label=u'E-mail')
    cidade = forms.CharField()
    estado = forms.ChoiceField(choices=STATE_CHOICES)
    mensagem = forms.CharField(widget=forms.Textarea())
