from django.urls import path
from . import views

app_name='tarefas'

urlpatterns = [
    path('listar_tarefas/', views.listar_tarefas, name='list-tasks'),
]