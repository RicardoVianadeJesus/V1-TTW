from django.forms import ModelForm
from app.models import Computador

class ComputadorForm(ModelForm):
    class Meta:
        model = Computador
        fields = ['equipamento', 'origem', 'setor', 'data', 'manutencao', 'status', 'dataSaida']