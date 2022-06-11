from django.db import models

class Ponto (models.Model):
    nome = models.CharField(max_length=200)
    bairro_localizado = models.CharField(max_length=200)
    horario_aberto = models.CharField(max_length=200)
    preco_minimo = models.DecimalField(max_digits=6, decimal_places=2)
    preco_gasto = models.DecimalField(max_digits=6, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField()
    criado_por = models.ForeignKey()

