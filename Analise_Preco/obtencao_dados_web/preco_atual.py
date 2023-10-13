# Função para achar o preço atual das ações.
# Para achar o preço do ativo no momento foi usado a técnica de web scraping.
# O site de onde os dados foram tirados é o yahoo finance.
import requests
from bs4 import BeautifulSoup
from ..models import Ativo
from decimal import Decimal
import datetime
from .analise_email import analise_limites_preco, enviar_email


def obter_preco_acao(nome_ativo):
    url = f'https://finance.yahoo.com/quote/{nome_ativo}.SA'

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        preco_atual = soup.find('fin-streamer', attrs={'data-symbol': f"{nome_ativo}.SA"})

        if preco_atual and 'value' in preco_atual.attrs:
            return preco_atual.attrs['value']
        else:
            return None
        
    except Exception as e:
        return None
    
# Função para atualizar o preço da ação a cada 5 minutos.
def atualizar_preco_acao():
    hora_atual = datetime.datetime.now().time()
    hora_inicial = datetime.time(10,0)
    hora_final = datetime.time(17,0)

    print("update")
    if hora_inicial <= hora_atual <= hora_final:
        ativos = Ativo.objects.all()
        for ativo in ativos:
            preco_atualizado = obter_preco_acao(ativo.nome_ativo)
            print(f"Preço atualizado para {ativo.nome_ativo}: {preco_atualizado}")
            if preco_atualizado:
                ativo.preco_atual = Decimal(preco_atualizado)
                ativo.save()
        
        Resultados = analise_limites_preco()
        enviar_email(Resultados)

    
