import pandas as pd
import os

# 1. Coleta de dados
nome = str(input("Digite o seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

# Criamos o dicionário sem colchetes nos valores para evitar que fiquem como "listas" no Excel
novos_dados = {
    "nome": nome,
    "idade": idade,
    "altura": altura
}

arquivo = "cadastro_alunos.xlsx"

# 2. Lógica para não sobrescrever o arquivo antigo
if os.path.exists(arquivo):
    # Se o arquivo já existe, lemos ele
    leitura_excel = pd.read_excel(arquivo)
    # Criamos um DataFrame com o novo usuário
    novo_df = pd.DataFrame([novos_dados])
    # Concatenamos (juntamos) o antigo com o novo
    tabela_atualizada = pd.concat([leitura_excel, novo_df], ignore_index=True)
else:
    # Se não existe, criamos o primeiro registro
    tabela_atualizada = pd.DataFrame([novos_dados])

# 3. Salvar no Excel
tabela_atualizada.to_excel(arquivo, index=False)

print("\n--- Cadastro Realizado com Sucesso ---")
print(tabela_atualizada)

# Exemplo de como apagar a última linha, se necessário:
# tabela_atualizada = tabela_atualizada.drop(tabela_atualizada.index[-1])
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 



               

