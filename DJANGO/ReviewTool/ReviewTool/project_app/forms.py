from django import forms
from .models import Project
from django.forms.widgets import SelectDateWidget, CheckboxSelectMultiple

class ProjectForm(forms.ModelForm):
  start_date = forms.DateField()
  class Meta:
    model = Project
    fields = ['name', 'business_field', 'customer', 'lead', 'start_date', \
            'end_date', 'viewers', 'creators', 'comment']