from django import forms

class CreateFakeDataForm(forms.Form):
  numbers = forms.DecimalField()
