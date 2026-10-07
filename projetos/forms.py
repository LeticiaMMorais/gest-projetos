from django import forms
from .models import *

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'data_inicio']
        labels = {'nome': 'Nome', 'descricao': 'Descrição', 'data_inicio': 'Data de início do projeto'}

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control'})
        }