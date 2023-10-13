import schedule
import time
from .obtencao_dados_web.preco_atual import atualizar_preco_acao

# Função para que a obtenção do preço da ação sempre fique ativa.
def run_schedule():
    schedule.every(1).minutes.do(atualizar_preco_acao)
    
    while True:
        schedule.run_pending()
        time.sleep(1)