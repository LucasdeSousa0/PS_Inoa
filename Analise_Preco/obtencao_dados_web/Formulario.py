from django import forms
from ..models import Ativo, Usuario
from django.core.exceptions import ValidationError

class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = ['nome_ativo', 'preco_compra', 'preco_venda', 'tunel', 'spread_superior', 'spread_inferior']

        def clean(self):
            cleaned_data = super().clean()
            
            tunel = cleaned_data.get('tunel')
            preco_compra = cleaned_data.get('preco_compra')
            preco_venda = cleaned_data.get('preco_venda')
            spread_superior = cleaned_data.get('spread_superior')
            spread_inferior = cleaned_data.get('spread_inferior')
            
            if tunel == 'ESTATICO':
                if spread_superior or spread_inferior:
                    raise ValidationError('Campos de "Preço a Mais" e "Preço a Menos" devem estar vazios para Túneis de Negociação "Estático"')
            elif tunel == 'DINAMICO':
                if preco_compra or preco_venda:
                    raise ValidationError('Campos de "Preço de Compra" e "Preço de Venda" devem estar vazios para Túneis de Negociação "Dinâmico"')

            return cleaned_data

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_usuario', 'email_usuario']