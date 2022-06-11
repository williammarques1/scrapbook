from django.db import models

class PontoTuristico (models.Model):
    nome = models.CharField(max_length=200)
    bairro_localizado = models.CharField(max_length=200)
    horario_visita = models.CharField(max_length=200)
    preco = models.IntegerField
    data_criacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField()
    viagens_realizadas = models.ForeignKey()
    criado_por = models.ForeignKey()

