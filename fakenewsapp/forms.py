from django import forms
from .models import Noticiascad

class NoticiascadForm(forms.ModelForm):
    class Meta:
     model = Noticiascad
     fields = '__all__'