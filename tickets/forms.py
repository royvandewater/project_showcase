from django import forms
from models import *

class NewTicketForm(forms.Form):
    name        = forms.CharField(max_length=255, required=True)
    priority    = forms.IntegerField()
    description = forms.CharField(max_length=512, widget=forms.Textarea)
