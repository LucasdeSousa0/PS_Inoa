from django.shortcuts import render, redirect
from .controllers.validacao_dados import validar_nomenclatura_ativo, validar_preco
from .controllers.existencia import existencia_ativo
from .models import Ativo
from Analise_Preco.obtencao_dados_web.Formulario import AtivoForm, UsuarioForm
from .scheduler import run_schedule
import threading

def home(request):
    return render(request,'home.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form =UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacao_cadastro')
    else:
        form = UsuarioForm()

    return render(request, 'cadastro.html', {'form': form})

def receber_ativos(request):

    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            nome_ativo = form.cleaned_data['nome_ativo']
            tunel_negociacao = form.cleaned_data['tunel']

            if tunel_negociacao == 'DINAMICO':
                if tunel_negociacao == 'DINAMICO':
                    spread_inferior = form.cleaned_data.get('spread_inferior')
                    spread_superior = form.cleaned_data.get('spread_superior')
                    preco_compra = 0.00
                    preco_venda = 0.00
            else:
                preco_compra = form.cleaned_data.get('preco_compra', 0.00)
                preco_venda = form.cleaned_data.get('preco_venda', 0.00)
                spread_superior = 0.00
                spread_inferior = 0.00

            if validar_nomenclatura_ativo(nome_ativo):
                if validar_preco(preco_compra, preco_venda, tunel_negociacao):
                    if existencia_ativo(nome_ativo):
                        ativo = Ativo.objects.create(
                            nome_ativo = nome_ativo,
                            preco_compra = preco_compra,
                            preco_venda = preco_venda,
                            spread_inferior = spread_inferior,
                            spread_superior = spread_superior,
                            tunel = tunel_negociacao,
                        )
                        return redirect('Ativo_certo')
                    else:
                        mensagem_de_erro = 'O ativo não existe na B3.'
                        return render(request, 'erro.html', {'mensagem_de_erro': mensagem_de_erro})
                else:
                    mensagem_de_erro = 'O preço de compra deve ser menor que o preço de venda.'
                    return render(request, 'erro.html', {'mensagem_de_erro': mensagem_de_erro})
            else:
                mensagem_de_erro = 'O nome do ativo não está de acordo com as regras da B3.'
                return render(request, 'erro.html', {'mensagem_de_erro': mensagem_de_erro})
        
    else:
        form = AtivoForm()

    return render(request, 'formulario_ativo.html', {'form': form})

def acompanhar_ativos(request):
    ativos = Ativo.objects.all()

    return render(request,'acompanhar_ativo.html', {'ativos': ativos})

def remover_ativo(request):
    if request.method == 'POST':
        ativo_remover = request.POST.getlist('ativos_selecionados')
        Ativo.objects.filter(id__in=ativo_remover).delete()

        return redirect('acompanhar-ativo')
    
    ativos = Ativo.objects.all()
    return render(request, 'remover_ativo.html', {'ativos': ativos})

def Ativo_certo(request):
    return render(request, 'Ativo_certo.html')

def confirmacao_cadastro(request):
    return render(request, 'confirmacao_cadastro.html')

scheduler_thread = threading.Thread(target=run_schedule)
scheduler_thread.start()
