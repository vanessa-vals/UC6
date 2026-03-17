#podemos dar um apelido a biblioteca que esta sendo usado
import pandas as pd #pd é o nome que eu dei a biblioteca



nome = str(input(f"Digite um nome: "))
idade = str(input("Digite sua idade: ")),
altura = float(input(f"Digite sua altura: ")),

#criação de dicionário deixando a opçao de preenchimento maleavel
dados = {
 "nome":[nome],
 "idade":[idade],
 "altura":[altura],
}

# Data.Frame para realizar a criação de um excel para que o pandas consiga utilizar para depois repassar os dados para a planilha
# to_excel() criar uma nova planilha, pega os dados digitados pelo usuário no DataFrame e gravar na planilha criada
excel = pd.DataFrame(dados)
excel.to_excel("UC06_Aula12.xlsx")
leitura_excel = pd.read_excel("UC06_Aula12.xlsx")
nova_linha = len(leitura_excel)

# Use as variáveis diretas, sem os colchetes do dicionário
leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
leitura_excel.loc[nova_linha, "altura"] = dados["altura"]

# Salvar a planilha (usando o 'r' para evitar erro de caminho)
leitura_excel.to_excel(r"UC06_Aula12\cadastro_alunos.xlsx", index=False)



               

