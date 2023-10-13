# Esse arquivo tem como objetivo validar os dados com as regras da B3, ou seja, ver se o nome /
# Está no padrão da B3 (4 letras) e um ou dois dígitos, de acordo com a regra

# Função para validar o nome do ativo está escrito de acordo com os padrões da B3
def validar_nomenclatura_ativo(nome):
    nome = nome.strip().upper()
    if len(nome) == 5 or len(nome) == 6:
        if len(nome) == 5:
            if nome[4].isdigit():
                return True
        elif len(nome) == 6:
            if nome[4:].isdigit():
                numero = int(nome[4:])
                if (numero >= 1 and numero <= 12) or numero in [32, 33, 34, 35]:
                    return True
    return False

# Função para validar se os preços do usuario estão no padrão.
def validar_preco(preco_compra,preco_venda, tunel):
    try:
        preco_compra = float(preco_compra)
        preco_venda = float(preco_venda)

        if tunel == 'ESTATICO':
            if (preco_compra * 100) % 1 == 0 and (preco_venda * 100) % 1 == 0:
                if preco_compra < preco_venda:
                    return True
        elif tunel == 'DINAMICO':
            return True
        
    except ValueError:
        pass

    return False