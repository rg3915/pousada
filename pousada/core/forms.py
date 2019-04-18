#biblioteca django para importar de model todos os formularios
from django.forms import ModelForm
from .models import Pessoa,Quarto, MovRotativo, Mensalista, MovMensalista


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class QuartoForm(ModelForm):
    class Meta:
        model = Quarto
        fields = '__all__'

class MovRotativoForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'

class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'

class MovMensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'