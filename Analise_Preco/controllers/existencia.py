# Essa função tem como objetivo ser um segundo método de conferência do código do ativo dado / 
# dado pelo usuário
import os

def existencia_ativo(nome_ativo):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'acoes_listadas_B3.txt')

    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            nome_ativo_linha = line.strip()
            if nome_ativo == nome_ativo_linha:
                return True
            
    return False