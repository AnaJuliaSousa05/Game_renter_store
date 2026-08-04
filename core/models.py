from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

class Jogo(models.Model):
    titulo = models.CharField(max_length=200)
    alugado = models.BooleanField(default=False)
    plataforma = models.CharField(max_length=50) 
    preco_diaria = models.DecimalField(max_digits=5, decimal_places=2) 

    def __str__(self):
        return self.titulo

class Locacao(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE) 
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE) #efeito cascata
    data_locacao = models.DateField(default=date.today)
    dias = models.PositiveIntegerField(default=1) # qtd de dias contratados 
    data_devolucao = models.DateField(blank=True, null=True) 
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True) 
    devolvido = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.valor_total and self.jogo:
            self.valor_total = self.jogo.preco_diaria * self.dias

        if not self.data_devolucao and self.jogo:
            self.data_devolucao = self.data_locacao + timedelta(days=self.dias)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cliente.username} alugou {self.jogo.titulo}"