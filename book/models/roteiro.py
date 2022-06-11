from django.db import models

class Roteiro (models.Model):
    viagens = models.ForeignKey()
    