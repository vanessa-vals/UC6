import pandas as pd
import os

# Nome do arquivo
arquivo = "base_BANCO_TABAJARA.xlsx"

# 1. CRIAR/PREENCHER ARQUIVO EXCEL (Se não existir)
if not os.path.exists(arquivo):
    colunas = ["nome_cliente", "tipo_conta", "numero_conta", "cpf", "agencia", "extrato_bancario", "deposito", "saque"]
    df_vazio = pd.DataFrame(columns=colunas)
    df_vazio.to_excel(arquivo, index=False)

# INÍCIO DO MENU PRINCIPAL
while True:
    print("\n" + "="*48)
    print("        BANCO TABAJARA - SISTEMA BANCÁRIO")
    print("="*48)
    print("  1 > Criar conta")
    print("  2 > Acessar conta")
    print("  0 > Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo... Obrigado por usar o Banco Tabajara!")
        break

    # --- OPÇÃO 1: CRIAR CONTA ---
    if opcao == "1":
        df_atual = pd.read_excel(arquivo)
        
        nome = input("Digite o nome do cliente: ").strip()
        cpf = input("Digite o CPF (apenas números): ").strip()
        tipo = input("Digite o tipo (Corrente/Poupança/Salário): ").strip().capitalize()

        total_clientes = len(df_atual)
        num_conta = 100 + total_clientes  
        agencia = 400 + total_clientes
        extrato_inicial = 0.0  

        nova_linha = {
            "nome_cliente": nome,
            "tipo_conta": tipo,
            "numero_conta": num_conta,
            "cpf": cpf,
            "agencia": agencia,
            "extrato_bancario": extrato_inicial,
            "deposito": 0.0,
            "saque": 0.0
        }

        df_atual = pd.concat([df_atual, pd.DataFrame([nova_linha])], ignore_index=True)
        df_atual.to_excel(arquivo, index=False)
        
        print("\n✅ CONTA CRIADA COM SUCESSO!")
        print(f"Cliente: {nome} | Conta: {num_conta} | Saldo: R$ {extrato_inicial:.2f}")

    # --- OPÇÃO 2: ACESSAR CONTA ---
    elif opcao == "2":
        df_atual = pd.read_excel(arquivo)
        busca_cpf = input("Digite o CPF para acessar: ").strip()
        
        filtro_cpf = df_atual[df_atual['cpf'].astype(str) == busca_cpf]

        if not filtro_cpf.empty:
            busca_conta = input("Agora, digite o número da conta: ").strip()
            conta_no_excel = str(filtro_cpf.iloc[0]['numero_conta'])

            if busca_conta == conta_no_excel:
                idx = filtro_cpf.index[0] 
                
                # LOOP DO MENU INTERNO DA CONTA
                while True:
                    df_atual = pd.read_excel(arquivo)
                    
                    # --- CORREÇÃO AQUI: astype(float) preenchido ---
                    df_atual['extrato_bancario'] = df_atual['extrato_bancario'].astype(float)
                    df_atual['saque'] = df_atual['saque'].astype(float)
                    df_atual['deposito'] = df_atual['deposito'].astype(float)

                    nome_c = df_atual.loc[idx, 'nome_cliente']
                    tipo_c = str(df_atual.loc[idx, 'tipo_conta']).strip().lower()
                    saldo_atual = float(df_atual.loc[idx, 'extrato_bancario'])

                    print(f"\n✅ Bem-vindo {nome_c} ao Banco Tabajara!")
                    print("1 - Saque")
                    print("2 - Depósito")
                    print("3 - Saldo")
                    print("0 - Sair da conta")

                    sub_opcao = input("Escolha uma opção: ")

                    if sub_opcao == "0":
                        break

                    # --- REGRA 1: SAQUE ---
                    elif sub_opcao == "1":
                        try:
                            valor_solicitado = float(input("Digite o valor para saque: R$ "))
                            
                            if valor_solicitado > saldo_atual:
                                print("\n❌ Valor maior que o disponivel em conta")
                                continue 
                            
                            if valor_solicitado <= 0:
                                print("\n❌ Valor inválido.")
                                continue

                            if "corrente" in tipo_c:
                                taxa_pct = 0.05
                                desc_taxa = "5% (Conta Corrente)"
                            elif "sal" in tipo_c: 
                                taxa_pct = 0.02
                                desc_taxa = "2% (Conta Salário)"
                            else: 
                                taxa_pct = 0.01
                                desc_taxa = "1% (Poupança/Outros)"

                            valor_taxa = round(valor_solicitado * taxa_pct, 2)
                            
                            if (valor_solicitado + valor_taxa) > saldo_atual:
                                print(f"❌ Saldo insuficiente para pagar a taxa de R$ {valor_taxa:.2f}")
                                continue

                            novo_saldo = round(saldo_atual - valor_solicitado - valor_taxa, 2)

                            df_atual.at[idx, 'extrato_bancario'] = novo_saldo
                            df_atual.at[idx, 'saque'] += valor_solicitado
                            df_atual.to_excel(arquivo, index=False)

                            print("================================================")
                            print("      Saque realizado com sucesso!")
                            print(f"      Saque: R$ {valor_solicitado:.2f}")
                            print(f"      Valor em conta: R$ {novo_saldo:.2f}")
                            print(f"      Taxa para saque: {desc_taxa}")
                            print(f"      Valor de desconto saque: R$ {valor_taxa:.2f}")
                            print("================================================\n")

                        except ValueError:
                            print("❌ Erro: Digite apenas números.")

                    # --- REGRA 2: DEPÓSITO ---
                    elif sub_opcao == "2":
                        try:
                            valor_dep = float(input("Digite o valor para depósito: R$ "))
                            
                            if valor_dep < 0:
                                print("\n❌ Numero invalido, operação encerrada")
                                continue
                            
                            novo_saldo = round(saldo_atual + valor_dep, 2)
                            
                            df_atual.at[idx, 'extrato_bancario'] = novo_saldo
                            df_atual.at[idx, 'deposito'] += valor_dep
                            df_atual.to_excel(arquivo, index=False)

                            print("================================================")
                            print(f"      Valor depositado: R$ {valor_dep:.2f}")
                            print(f"      Saldo em conta: R$ {novo_saldo:.2f}")
                            print("================================================\n")
                        except ValueError:
                            print("❌ Erro: Digite apenas números.")

                    # --- REGRA 3: SALDO ---
                    elif sub_opcao == "3":
                        print("================================================")
                        print(f"   Tipo conta: {df_atual.loc[idx, 'tipo_conta']}")
                        print(f"   Saldo em conta: R$ {saldo_atual:.2f}")
                        print("================================================\n")

                    else:
                        print("❌ Opção inválida.")
            else:
                print("❌ Acesso negado: O número da conta não confere com o CPF.")
        else:
            print("❌ CPF não encontrado no sistema.")

    else:
        if opcao != "0":
            print("❌ Opção principal inválida.")