nome = []
idade = []


nome = str(input(f"Digite um nome: "))
idade = str(input(f"Digite sua idade: "))

arquivo = (nome, idade)

with open("cadastros.txt", "a") as arquivo:
 arquivo.write(nome + "-" + idade + "\n") 




