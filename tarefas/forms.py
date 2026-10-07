from django import forms
from .models import *

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa

        fields = ['titulo', 'descricao', 'prioridade', 'concluido', 'projeto']

        labels = {
            'titulo':'Título da tarefa:', 
            'descricao':'Descrição da tarefa:', 
            'prioridade':'Prioridade:',
            'concluido':'Concluído:', 
            'projeto':'Projeto associado:'
        }

        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'prioridade': forms.Select(attrs={'class': 'form-select'}),
            'concluido': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'projeto': forms.Select(attrs={"class": 'form-select'}),
        }
        

