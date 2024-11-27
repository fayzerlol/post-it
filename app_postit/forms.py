from django import forms
from .models import Planilha, Quadro

class FormularioUploadPlanilha(forms.ModelForm):
    class Meta:
        model = Planilha
        fields = ['arquivo']


class QuadroForm(forms.ModelForm):
    class Meta:
        model = Quadro
        fields = ['nome', 'descricao']

class ImportarPlanilhaForm(forms.Form):
    colunas_disponiveis = forms.MultipleChoiceField(
        choices=[], widget=forms.CheckboxSelectMultiple, required=True
    )
    colunas_no_card = forms.MultipleChoiceField(
        choices=[], widget=forms.CheckboxSelectMultiple, required=False
    )

    def __init__(self, *args, **kwargs):
        colunas = kwargs.pop('colunas', [])
        super().__init__(*args, **kwargs)
        self.fields['colunas_disponiveis'].choices = [(col, col) for col in colunas]
        self.fields['colunas_no_card'].choices = [(col, col) for col in colunas]