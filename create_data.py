import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pousada.settings")
django.setup()

from random import choice, randint
from pousada.hotel.models import Quarto, Padrao


def criar_quartos():
    Quarto.objects.all().delete()
    titulos = ('Double', 'Especial', 'Simples', 'Duplo', 'Luxo', 'Vip')
    aux = []
    padroes = Padrao.objects.all()
    for item in range(1, 21):
        titulo = choice(titulos)
        padrao = choice(padroes)
        valor_diaria = randint(80, 400)
        obj = Quarto(
            numero=item,
            titulo=titulo,
            padrao=padrao,
            valor_diaria=valor_diaria
        )
        aux.append(obj)
    Quarto.objects.bulk_create(aux)


criar_quartos()
