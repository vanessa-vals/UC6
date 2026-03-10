
# toda conexão com arquivo externo sempre nas primeiras linhas da pagina da programação
import random
import math
import datetime

# biblioteca sorteio
#gerar numero aleatorio ao estilo sorteio com a função random

numero_aleatorio = random.randint(1000, 2000)
print(numero_aleatorio)


#sorteio em caso de lista, dicionario e palavras
alunos = ["Israel","Adenilson", "Anna", "Welligton", "Vanessa", "Iara", "Camila"]
sorteado = random.choice(alunos)
sorteado2 = random.choice(alunos)
print("Dupla dinamica", sorteado, "-", sorteado2)

# biblioteca matematica



#raiz quadrada
numero = 2
raiz = math.sqrt(numero)
print(raiz)

#elevar um numero
print(math.pow(2, 2))

#trabalhando com datas 
agora = datetime.datetime.now()
print(agora.second)

"""
excercicio
Solicitar ao usuário um numero de 1 a 4 
gerar um numero aleatorio usando a bibliotcarandom radint
verificar se o usuário digitou o mesmo valor que o resutado da função
"""

nome_usuario = str(input("Digite seu nome: "))
numero_usuario = int(input("Digite um numero da sorte de 1 a 5: "))
numero_sorte = random.randint(1, 5)
if numero_sorte == numero_sorte:
    print("Parabéns", nome_usuario,"você ganhou !!!")
else: 
    print("Errou, tentou")



