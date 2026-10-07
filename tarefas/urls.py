from django.urls import path
from . import views

app_name='tarefas'

urlpatterns = [
    path('listar_tarefas/', views.listar_tarefas, name='list-tasks'),
    path('ver_detalhes/<int:id>', views.detalhes_tarefa, name='task-detail'),
    path('criar_tarefa/', views.criar_tarefa, name='create-task'),
    path('editar_tarefa/<int:id>/', views.editar_tarefa, name='edit-task'),
    path('excluir_tarefa/<int:id>/', views.excluir_tarefa, name='delete-task'),
]