import pandas as pd
import os

# Nome do arquivo de banco de dados
arquivo = "base_BANCO_TABAJARA.xlsx"

# Se não existe cria um novo DataFrame vazio
if not os.path.exists(arquivo):
    df_vazio = pd.DataFrame(columns=["nome_cliente", "tipo_conta", "numero_conta", "cpf", "agencia", "extrato_bancario"])
    df_vazio.to_excel(arquivo, index=False)

while True:
    print("\n" + "="*48)
    print("      BANCO TABAJARA - ACESSE SUA CONTA")
    print("="*48)
    print("  1 > Criar conta")
    print("  2 > Acessar conta")
    print("  0 > Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Carrega a base atual
        df_atual = pd.read_excel(arquivo)
        
        nome = str(input("Digite o seu nome de cliente: "))
        cpf = str(input("Digite o CPF: "))
        tipo = str(input("Digite o tipo de conta (Corrente/Poupança/Salário): "))
        i = 1

        # Lógica para criar número de conta e agência automático
        total_clientes = len(df_atual)
        num_conta = total_clientes + 1
        agencia = 400 + i  # Exemplo de agência fixa ou lógica incremental
        proxima_agencia = min(400 + total_clientes, 700)
        extrato_bancario = 0 + 1
        

        # Criando o dicionário com a nova linha
        nova_linha = {
            "nome_cliente": nome,
            "tipo_conta": tipo,
            "numero_conta": f"0{num_conta}",
            "cpf": cpf[:11],
            "agencia": proxima_agencia,
            "extrato_bancario": f"0{extrato_bancario}"
        }

        # Adiciona a nova linha ao DataFrame e salva no Excel
        df_atual = pd.concat([df_atual, pd.DataFrame([nova_linha])], ignore_index=True)
        df_atual.to_excel(arquivo, index=False)
        
        print(f"\n✅ Conta criada com sucesso! Número da conta: {num_conta}")

    elif opcao == "2":
        df_atual = pd.read_excel(arquivo)
        cpf_digitado = int(input("Digite CPF: "))
        conta_digitada = int(input("Digite o número da conta: "))
        
        # Filtra o DataFrame para buscar o cliente
        cliente = df_atual[(df_atual['cpf'] == cpf_digitado) & (df_atual['numero_conta'] == conta_digitada)]
        
        if not cliente.empty:
            nome_cliente = cliente.iloc[0]['nome_cliente']
            print(f"\n🏦 Bem-vindo(a), {nome_cliente}!")
            # Aqui você pode adicionar o menu interno da conta (Saque, Depósito, etc.)
        else:
            print("\n⚠️ Usuário não encontrado ou dados incorretos.")

    elif opcao == "0":
        print("Saindo... Obrigado por usar o Banco Tabajara! 👋")
        break
        
    else:
        print("\n❌ Opção inválida! Tente novamente.")