from django.db import models


class TipoDocumento(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    ultimo_numero = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

    def proximo_numero(self):
        return self.ultimo_numero + 1
