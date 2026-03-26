
#chamar bibliotecas
import pandas as pd
import os

# nome do arquivo a ser criado
arquivo = "base_BANCO_TABAJARA.xlsx"

# criar/preencher arquivo excell
if not os.path.exists(arquivo):
    colunas = ["nome_cliente", "tipo_conta", "numero_conta", "cpf", "agencia", "extrato_bancario", "deposito", "saque"]
    df_vazio = pd.DataFrame(columns=colunas)
    df_vazio.to_excel(arquivo, index=False)

#inicio menu
while True:
    print("\n" + "="*48)
    print("        BANCO TABAJARA - SISTEMA BANCÁRIO")
    print("="*48)
    print("  1 > Criar conta")
    print("  2 > Acessar conta")
    print("  0 > Sair")
    
    #escolher opção
    opcao = input("Escolha uma opção: ")


    # se opção 1
    if opcao == "1":
        df_atual = pd.read_excel(arquivo)
        
        # sados usuário
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF: ")
        tipo = input("Digite o tipo (Corrente/Poupança/Salário): ")

        # sógica /regras
        total_clientes = len(df_atual)
        num_conta = min(0 + total_clientes, 100) # limite de 100 
        agencia = min(400 + total_clientes, 700) # de 400 de 700 
        extrato_inicial = f"'0{total_clientes}" # extrato com 0 no inicio
       

        #dados para o excell
        nova_linha = {
            "nome_cliente": nome,
            "tipo_conta": tipo,
            "numero_conta": num_conta,
            "cpf": cpf,
            "agencia": agencia,
            "extrato_bancario": extrato_inicial, 
            "deposito": 0,
            "saque": 0
        }

        # salvar no excel
        df_atual = pd.concat([df_atual, pd.DataFrame([nova_linha])], ignore_index=True)
        df_atual.to_excel(arquivo, index=False)
        
        #mensagem no terminal de ok
        print("\n✅ CONTA CRIADA COM SUCESSO!")
        print(f"Cliente: {nome} | CPF: {cpf} | Tipo: {tipo}")
        print(f"Conta: {num_conta} | Agência: {agencia} | Extrato: {extrato_inicial}")

    #se opção 2
    elif opcao == "2":
        df_atual = pd.read_excel(arquivo)
        
       #solicita CPF e CONTA
        busca_cpf = input("Digite o CPF para acessar: ")
        
        # 2. Primeiro, filtramos apenas pelo CPF para ver se ele existe
        filtro_cpf = df_atual[df_atual['cpf'].astype(str) == busca_cpf]

        if not filtro_cpf.empty:
            # Se o CPF existe, agora pedimos a conta
            busca_conta = input("Agora, digite o número da conta: ")
            
            # Pegamos o valor da conta que está no Excel (índice 0 do filtro)
            conta_no_excel = str(filtro_cpf['numero_conta'].values[0])
            
            # 3. Validamos se a conta digitada bate com a do Excel
            if busca_conta == conta_no_excel:
                # Pegamos o índice (linha) real no DataFrame original
                idx = filtro_cpf.index[0]
                
                # CORREÇÃO DO .LOC: precisa da linha (idx) e da coluna
                nome = df_atual.loc[idx, 'nome_cliente']
                
                print(f"\n✅ Bem-vindo {nome} ao Banco Tabajara!")
                
                # Aqui você seguiria com as opções de Saque/Depósito...
            else:
                print("❌ Acesso negado: O número da conta não confere com o CPF.")
        else:
            print("❌ CPF não encontrado no sistema.")