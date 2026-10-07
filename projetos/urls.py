from django.urls import path, include
from .views import *

urlpatterns = [
    path('listar-projetos/', listar_projetos, name='list-projects'),
    path('criar-projeto/', criar_projeto, name='create-project'),
    path('detalhes-projeto/<int:id>', detalhes_projeto, name='project-detail'),
    path('editar-projeto/<int:id>', editar_projeto, name='edit-project'),
    path('excluir-projeto/<int:id>', excluir_projeto, name='delete-project'),
]
