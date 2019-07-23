from django.forms import ModelForm
from .models import Pessoa, Quarto, Reserva, Mensalista, MovMensalista


class PessoaForm(ModelForm):

    class Meta:
        model = Pessoa
        fields = '__all__'


class QuartoForm(ModelForm):

    class Meta:
        model = Quarto
        fields = '__all__'


class ReservaForm(ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'


class MensalistaForm(ModelForm):

    class Meta:
        model = Mensalista
        fields = '__all__'


class MovMensalistaForm(ModelForm):

    class Meta:
        model = MovMensalista
        fields = '__all__'
