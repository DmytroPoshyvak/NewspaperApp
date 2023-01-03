from django import forms
from . import models

class ComentForm(forms.ModelForm):
    class Meta:
        model = models.Coment
        fields = ['comment']
