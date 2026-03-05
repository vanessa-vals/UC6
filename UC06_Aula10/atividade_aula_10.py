nome = []
idade = []

with open("cadastros.txt", "a") as arquivo:
   arquivo.write(nome, "-" , idade, "\n")


for i in range(3):
    nome = str(input(f"Digite um nome: "))
    idade = int(input(f"Digite sua idade: "))
   



