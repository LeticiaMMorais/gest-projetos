from django.shortcuts import render
from django.db import models
from .models import *

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    contexto={
        'tarefas': tarefas,
    }
    return render(request, 'tarefas/list_tasks.html', context=contexto)