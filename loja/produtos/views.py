from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Função para cadastrar um novo item
def cadastrar_item(request):
    # Verifica se a requisição é POST (enviando dados do formulário)
    if request.method == 'POST':
        # Cria um formulário a partir dos dados enviados
        form = ItemForm(request.POST)
        
        # Se o formulário for válido, salva o novo item no banco de dados
        if form.is_valid():
            form.save()
            # Redireciona para a página de lista de itens
            return redirect('listar_itens')
    else:
        # Se não for POST, cria um formulário vazio
        form = ItemForm()

    # Renderiza o template 'cadastrar.html', passando o formulário
    return render(request, 'cadastrar.html', {'form': form})

# Função para listar todos os itens cadastrados
def listar_itens(request):
    # Pega todos os itens do banco de dados
    itens = Item.objects.all()
    
    # Renderiza o template 'listar.html' passando a lista de itens
    return render(request, 'listar.html', {'itens': itens})

# Função para deletar um item específico
def deletar_item(request, id):
    # Tenta pegar o item com o id fornecido. Se não encontrar, retorna 404
    item = get_object_or_404(Item, id=id)
    
    # Deleta o item do banco de dados
    item.delete()
    
    # Redireciona para a página de lista de itens
    return redirect('listar_itens')  # volta para a lista
