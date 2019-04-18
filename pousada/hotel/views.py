from django.shortcuts import render
from .models import Contato


# def home(request):
#     return render(request, 'hotel/index.html')


# def contato(request):
#     try:
#         contato = {}
#         contato['email'] = request.POST.get('email')
#         contato['nome'] = request.POST.get('nome')
#         contato['sobrenome'] = request.POST.get('sobrenome')
#         contato['endereco'] = request.POST.get('endereco')
#         contato['mensagem'] = request.POST.get('mensagem')
#         contato['receber'] = True if request.POST.get(
#             'email') == 'on' else False

#         Contato.objects.create(**contato)
#     except Exception as e:
#         mensagem = str(e)
#         print(mensagem)
#     else:
#         mensagem = 'contato realizado com sucesso'
#     return render(request, 'hotel/contato.html', {'mensagem': mensagem})


# def servicos(request):
#     return render(request, 'hotel/servicos.html')
