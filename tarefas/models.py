from django.db import models
from projetos.models import *

class Tarefa(models.Model):
    PRIORITY_CHOICES = [
        ('baixa', 'Baixa'),
        ('normal', 'Normal/Média'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]

    titulo = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(max_length=500, null=True, blank=True)
    prioridade = models.CharField(choices=PRIORITY_CHOICES)
    concluido = models.BooleanField(null=False)
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='tarefa',
    )

    def __str__(self):
        return self.titulo