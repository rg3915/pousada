import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pousada.settings")
django.setup()

import string
import timeit
from django.utils.text import slugify
from mixer.backend.django import mixer
from random import choice, randint
from pousada.hotel.models import Quarto, Padrao, Pessoa


def gen_digits(max_length):
    return str(''.join(choice(string.digits) for i in range(max_length)))


def gen_phone():
    # gera um telefone no formato xx xxxxx-xxxx
    digits_ = gen_digits(11)
    return '{} 9{}-{}'.format(digits_[:2], digits_[3:7], digits_[7:])


def gen_city():
    list_city = [
        [u'São Paulo', 'SP'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Goiânia', 'GO'],
        [u'Guarulhos', 'SP'],
        [u'Brasília', 'DF'],
        [u'Campinas', 'SP'],
        [u'Fortaleza', 'CE'],
        [u'São Luís', 'MA'],
        [u'Belo Horizonte', 'MG'],
        [u'São Gonçalo', 'RJ'],
        [u'Manaus', 'AM'],
        [u'Maceió', 'AL'],
        [u'Duque de Caxias', 'RJ'],
        [u'Recife', 'PE'],
        [u'Natal', 'RN'],
        [u'Porto Alegre', 'RS'],
        [u'Campo Grande', 'MS']]
    return choice(list_city)


def criar_clientes():
    Pessoa.objects.all().delete()
    aux = []
    for _ in range(10):
        nome = mixer.faker.name()
        email = slugify(nome) + '@email.com'
        cpf = gen_digits(14)
        cidade = gen_city()
        email = slugify(nome)
        telefone = gen_phone()
        obj = Pessoa(
            nome=nome,
            email=email,
            cpf=cpf,
            cidade=cidade[0],
            estado=cidade[1],
            telefone=telefone,
        )
        aux.append(obj)
    Pessoa.objects.bulk_create(aux)


PADROES = ('Luxo', 'King', 'Solteiro', 'Casal Simples',
           'Casal Especial', 'Solteiro Básico', 'Vip')


def criar_padroes():
    Padrao.objects.all().delete()
    aux = []
    for padrao in PADROES:
        obj = Padrao(nome=padrao)
        aux.append(obj)
    Padrao.objects.bulk_create(aux)


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


tic = timeit.default_timer()
criar_clientes()
criar_padroes()
criar_quartos()
toc = timeit.default_timer()
print('Time:', round(toc - tic, 2), 's')
