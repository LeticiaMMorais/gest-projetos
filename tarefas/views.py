from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import *
from . import forms

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    contexto={
        'tarefas': tarefas,
    }
    return render(request, 'tarefas/list_tasks.html', context=contexto)

def detalhes_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    return render(request, 'tarefas/task_detail.html', {'tarefa': tarefa})

def criar_tarefa(request):
    if request.method == 'POST':
        form = forms.TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas:list-tasks')
    else:
        form = forms.TarefaForm()
    return render(request, 'tarefas/create_tasks.html', {'form': form,})

def editar_tarefa(request, id):

    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        form = forms.TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefas:list-tasks')
    else:
        form = forms.TarefaForm(instance=tarefa)

    return render(request, 'tarefas/create_tasks.html', {'form': form})

def excluir_tarefa(request, id):
    print('id=', id)
    tarefas = Tarefa.objects.all()
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()

    return render(request, 'tarefas/list_tasks.html', {'tarefas': tarefas})