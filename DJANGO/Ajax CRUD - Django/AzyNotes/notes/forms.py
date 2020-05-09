from django import forms
from .models import Note


class CreateNotesForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['title']
