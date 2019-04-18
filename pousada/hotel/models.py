from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField('endereço', max_length=100)
    mensagem = models.TextField()
    receber = models.BooleanField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
