from ..models import Ativo, Usuario
import smtplib
import email.message

# Função para analisar condições para análise se o ativo atingiu as condições para enviar email
def analise_limites_preco():
    ativos = Ativo.objects.all()
    Resultados = [] #Vai marcar que tipo de email vai ser mandado: 0-> não mandar email, /
    # 1-> mandar email para compra , 2-> mandar email para venda

    for ativo in ativos:
        preco_compra_aux = ativo.preco_compra
        preco_venda_aux = ativo.preco_venda
        preco_atual = ativo.preco_atual
        limite_superior = ativo.spread_superior
        limite_inferior = ativo.spread_inferior

        if preco_compra_aux != 0 and preco_venda_aux != 0:
            if preco_atual <= preco_compra_aux:
                Codificador = 1
            elif preco_atual >= preco_venda_aux:
                Codificador = 2
            else:
                Codificador = 0

            if ativo.tunel == 'DINAMICO':
                if limite_inferior is not None:
                    ativo.preco_compra = preco_atual - limite_inferior
                if limite_superior is not None:
                    ativo.preco_venda = preco_atual + limite_superior
                ativo.save()
        else:
            if limite_inferior is not None:
                ativo.preco_compra = preco_atual - limite_inferior
            if limite_superior is not None:
                ativo.preco_venda = preco_atual + limite_superior
            ativo.save()

        Resultados.append(Codificador)
    
    return Resultados

# Função para enviar email
def enviar_email(resultados):
    usuario = Usuario.objects.first()
    nome_do_usuario = usuario.nome_usuario
    email_do_usuario = usuario.email_usuario
    ativos = Ativo.objects.all()

    for codificador, ativo in zip(resultados, ativos):
        if codificador != 0:
    
            if codificador == 1:
                corpo_email = f"""
                <p>Prezado {nome_do_usuario},</p>

                <p>Espero que este email o encontre bem. Gostaríamos de informar que o ativo <strong>{ativo.nome_ativo}</strong> listado na bolsa de valores atingiu o preço de compra que você especificou em sua conta.</p>

                <p>Detalhes do Ativo:</p>
                <ul>
                    <li>Ativo: <strong>{ ativo.nome_ativo }</strong></li>
                    <li>Preço Atual: <strong>{ ativo.preco_atual }</strong></li>
                </ul>

                <p>Isso significa que as condições para a compra desse ativo foram atendidas de acordo com as suas instruções. Se você deseja prosseguir com a compra, entre em contato conosco o mais breve possível para confirmar a transação. Caso contrário, não hesite em ignorar este aviso.</p>

                <p>Lembramos que os investimentos na bolsa de valores têm riscos associados, e é importante considerar cuidadosamente suas decisões de investimento. Se você tiver alguma dúvida ou precisar de assistência adicional, nossa equipe de suporte está à disposição para ajudar.</p>

                <p>Agradecemos por confiar em nossos serviços e estamos à disposição para fornecer qualquer suporte necessário.</p>

                <p>Atenciosamente,</p>
                <p><strong>[Nome da Empresa]</strong></p>
                <p><strong>[Informações de Contato]</strong></p>
                """
            else:
                corpo_email = f"""
                <p>Prezado {nome_do_usuario},</p>

                <p>Espero que este email o encontre bem. Gostaríamos de informar que o ativo <strong>{ ativo.nome_ativo }</strong> listado na bolsa de valores atingiu o preço de venda que você especificou em sua conta.</p>

                <p>Detalhes do Ativo:</p>
                <ul>
                    <li>Ativo: <strong>{ ativo.nome_ativo }</strong></li>
                    <li>Preço Atual: <strong>{ativo.preco_atual }</strong></li>
                </ul>

                <p>Isso significa que as condições para a venda desse ativo foram atendidas de acordo com as suas instruções. Se você deseja prosseguir com a venda, entre em contato conosco o mais breve possível para confirmar a transação. Caso contrário, não hesite em ignorar este aviso.</p>

                <p>Lembramos que os investimentos na bolsa de valores têm riscos associados, e é importante considerar cuidadosamente suas decisões de investimento. Se você tiver alguma dúvida ou precisar de assistência adicional, nossa equipe de suporte está à disposição para ajudar.</p>

                <p>Agradecemos por confiar em nossos serviços e estamos à disposição para fornecer qualquer suporte necessário.</p>

                <p>Atenciosamente,</p>
                <p><strong>[Nome da Empresa]</strong></p>
                <p><strong>[Informações de Contato]</strong></p>
                """

            msg = email.message.Message()
            msg['Subject'] = "Alerta do mercado"
            msg['From'] = email_do_usuario
            msg['To'] = 'lucasdesousa9.42@gmail.com' # adicionar email remetente
            password = 'lrwrresckntywmyg'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)

            s = smtplib.SMTP('smtp.gmail.com:587')
            s.starttls()
            s.login(msg['From'], password)
            s.sendmail(msg['From'],[msg['To']], msg.as_string().encode('utf-8'))
        else:
            continue


    