from django.shortcuts import render
from projetos import models
from tarefas import models

# Create your views here.
def home(request):
    projects = models.Projeto.objects.all()
    tasks = models.Tarefa.objects.all()

    return render(request, 'core/home.html', {'count_projects': len(projects), 'projects': projects, "count_tasks": len(tasks)},)