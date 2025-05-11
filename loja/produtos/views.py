from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def cadastrar_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)  # recebe arquivo aqui
        if form.is_valid():
            form.save()
            return redirect('listar_itens')
    else:
        form = ItemForm()
    return render(request, 'cadastrar.html', {'form': form})

def listar_itens(request):
    itens = Item.objects.all()
    return render(request, 'listar.html', {'itens': itens})

def deletar_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('listar_itens')
