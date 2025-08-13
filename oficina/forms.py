from django import forms
from .models import Motorista,ServicoManutencao


class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ["nome", "cpf"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome completo"}),
            "cpf": forms.TextInput(attrs={"class": "form-control", "placeholder": "Somente números", "maxlength": 11}),
        }

from django import forms
from .models import ServicoManutencao

class ServicoManutencaoForm(forms.ModelForm):
    class Meta:
        model = ServicoManutencao
        fields = ['veiculo', 'oficina', 'motorista', 'data_servico', 'descricao']
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-select'}),
            'oficina': forms.Select(attrs={'class': 'form-select'}),
            'motorista': forms.Select(attrs={'class': 'form-select'}),
            'data_servico': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
     