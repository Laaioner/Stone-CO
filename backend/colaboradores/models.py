from django.db import models

# Create your models here.
class Colaborador(models.Model):
    nome = models.CharField(max_length=80)
    nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    cpf = models.TextField(max_length=11)
    email = models.CharField(max_length=100)
    