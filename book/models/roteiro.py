from django.db import models

from scrapbook.book.models.visita import Visita

class Roteiro (models.Model):
    viagens = models.ForeignKey(Visita, models.CASCADE, related_name='visitas')
    