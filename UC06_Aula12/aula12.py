#podemos dar um apelido a biblioteca que esta sendo usado
import pandas as pd #pd é o nome que eu dei a biblioteca


nome = []
idade = []
altura = []

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
excel.to_excel("UC06_Aula12")
leitura_excel = pd.read_excel("UC06_Aula12.xlsx")
nova_linha = len(leitura_excel)

# Agora o tipo de dados coincide: número com número!
leitura_excel.loc[3, "nome"] = nome
leitura_excel.at[3, "idade"] = idade
leitura_excel.at[3, "altura"] = altura



               

