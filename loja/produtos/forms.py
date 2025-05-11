from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'preco', 'descricao', 'imagem']

def clean_imagem(self):
    imagem = self.cleaned_data.get('imagem')

    # Primeiro 'if': Checa se a imagem existe
    if imagem:
        # Segundo 'if': Se a imagem existe, checa se o tamanho é maior que 2MB
        if imagem.size > 2 * 1024 * 1024:  # 2MB
            raise forms.ValidationError("Imagem muito grande! Máx: 2MB.")
    
    return imagem
