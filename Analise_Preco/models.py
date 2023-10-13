from django.db import models

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)
    email_usuario = models.EmailField(unique=True)

TUNEL_CHOICES = [
    ('ESTATICO', 'Estático'),
    ('DINAMICO', 'Dinâmico Síncronos')
]

class Ativo(models.Model):
    nome_ativo = models.CharField(max_length=12)
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    preco_atual = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    tunel = models.CharField(max_length=8, choices=TUNEL_CHOICES, default='ESTATICO')
    spread_superior = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    spread_inferior = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
