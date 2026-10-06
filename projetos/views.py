from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ProjectsForm

# Create your views here.
def listar_projetos(request):
    projetos = Projeto.objects.all().order_by('data_inicio')

    return render(request, 'projetos/list_projects.html', {'projetos': projetos})

def detalhes_projeto(request, id):
    project = get_object_or_404(Projeto, id=id)

    return render(request, 'projetos/project_detail.html', {'projeto': project})

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list-projects')
    else:
        form = ProjectsForm()

    return render(request, 'projetos/create_projects.html', {'form': form})