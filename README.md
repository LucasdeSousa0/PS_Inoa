# Processo Seletivo INOA Sistemas

Este projeto foi desenvolvido como parte do processo seletivo para a INOA Sistemas. Aqui, todas as funcionalidades e recursos solicitados, bem como instruções para configurar e executar o projeto localmente.

## Pré-requisitos

- Python 3.12.0
- Django==4.2.6

As dependências também estão no `requirements.txt`.

- pip install asgiref
- pip install beautifulsoup4
- pip install bs4
- pip install certifi
- pip install charset-normalizer
- pip install django-crontab
- pip install idna
- pip install requests
- pip install schedule
- pip install soupsieve
- pip install sqlparse
- pip install tzdata
- pip install urllib3

## Uso

#### Migrations:

Antes de rodar o projeto, é importante realizar as migrations para construir o banco de dados.
```bash
python manage.py makemigrations
python manage.py migrate
```
#### Rodar o servidor:
Para iniciar o programa basta dar o seguinte comando:
```bash
python manage.py runserver
```

#### Como usar o programa:

Após rodar o servidor, na página principal tem acessos aos links para cadastrar o usuário, cadastrar o ativo, acompanhar os ativos já cadastrados e remover um ativo previamente cadastrado.

-  Cadastrar usuário: nessa página terá dois espaços, um para o nome do cliente e outro para o cadastro do email.
-  Cadastrar ativo: código do ativo na bolsa de valores (apenas ações), escolher o túnel de negociação, ou o preço de compra e venda, ou a distância ao preço atual.
-  Remover ativo: escolher entre os ativos cadastrados remover um deles
-  acompanhar ativo: ver os ativos já cadastrados com o preço de compra e venda, e preço atual

#### Funcionalidades:

Como o programa executa as funções:

- O preço atual é atualizado a cada 1 min.
- O modo como o preço atual é obtido é por meio de web scraping da página do Yahoo Finance


 


