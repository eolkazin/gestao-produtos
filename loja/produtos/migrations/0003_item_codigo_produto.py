# Generated by Django 5.2.1 on 2025-05-12 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_item_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='codigo_produto',
            field=models.CharField(default='TEMP001', max_length=20, unique=True),
        ),
    ]
