# Generated by Django 4.2.6 on 2023-10-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analise_Preco', '0004_remove_ativo_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='ativo',
            name='spread_inferior',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='ativo',
            name='spread_superior',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ativo',
            name='preco_compra',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='ativo',
            name='preco_venda',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
