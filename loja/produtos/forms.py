from django import forms
from .models import Item

# Formulário para o modelo Item
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item  # Especifica que o formulário está baseado no modelo 'Item'
        fields = ['nome', 'preco', 'descricao']  # Define quais campos do modelo serão exibidos no formulário
