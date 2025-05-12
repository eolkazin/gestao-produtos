from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='itens/', null=True, blank=True)
    codigo_produto = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

