from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from .models import Contato


@login_required
def dashboard(request):
    return render(request, 'hotel/dashboard.html')


@login_required
def pessoas(request):
    return render(request, 'hotel/pessoas.html')


@login_required
def quartos(request):
    return render(request, 'hotel/quartos.html')


@login_required
def rotativos(request):
    return render(request, 'hotel/rotativos.html')


@login_required
def mensalistas(request):
    return render(request, 'hotel/mensalistas.html')
