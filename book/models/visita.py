from xmlrpc.client import MAXINT
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from scrapbook.book.models.ponto import Ponto

class Visita (models.Model):
    horario_visita = models.CharField(max_length=200)
    total_gasto = models.DecimalField(max_digits=6, decimal_places=2)
    data_visita = models.DateTimeField()
    ponto_visitado = models.ForeignKey(Ponto)
    nota_ponto = models.IntegerField(validators=
        [MaxValueValidator(5),MinValueValidator(0)])
    descricao = models.CharField(max_length=1000)