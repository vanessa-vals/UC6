import pandas as pd


print("================================================")
print("        BEM - VINDO AO PORTAL DE ALUNOS")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > Criar")
print("         2 > Adicionar")
print("         3 > Apagar")
opcao = int(input("R: "))


if opcao == 1:
    print("Opção 1 selecionada")
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    dados = {
        "nome": [nome],
        "idade": [idade],
        "altura": [altura]
    }

    excel = pd.DataFrame(dados)

    excel.to_excel("Alunos.xlsx", index=False)
    print("Ação Finalizada....")

elif opcao == 2:
    print("Opção 2 selecionada...")
    print("Para a proxima aula")
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    dados = {
        "nome": [nome],
        "idade": [idade],
        "altura": [altura]
    }

    leitura_excel = pd.read_excel("Alunos.xlsx")
    nova_linha = len(leitura_excel)

    leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
    leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
    leitura_excel.loc[nova_linha, "altura"] = dados["altura"]


    leitura_excel.to_excel("Alunos.xlsx", index=False)
    print("Ação finalizada.....")

elif opcao == 3:
    print("Opção 3 selecionada")
    linha_apagada = int(input("Digite um número inteiro: "))

    leitura_excel = pd.read_excel("Alunos.xlsx")

    leitura_excel = leitura_excel.drop(linha_apagada)

    leitura_excel.to_excel("Alunos.xlsx", index=False)
    print("Ação finalizada.....")



               

