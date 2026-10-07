from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tarefas/', include('tarefas.urls', namespace='tarefas')),
]
