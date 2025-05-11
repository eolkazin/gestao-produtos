from django.db import models

# Definindo a classe 'Item', que representará os itens no banco de dados
class Item(models.Model):
    
    # Atributo 'nome' para armazenar o nome do item, com limite de 100 caracteres
    nome = models.CharField(max_length=100)
    
    # Atributo 'preco' para armazenar o preço do item, com até 10 dígitos no total e 2 após a vírgula
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Atributo 'descricao' para armazenar a descrição do item, sem limite de tamanho
    descricao = models.TextField()

    # Método especial para exibir o nome do item quando a instância for convertida para string
    def __str__(self):
        return self.nome
