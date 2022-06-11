from django.db import models

class Viagem (models.Model):
    horario_viagem = models.CharField(max_length=200)
    total_gasto = models.IntegerField
    data_viagem = models.DateTimeField()
    ponto_turistico = models.ForeignKey()