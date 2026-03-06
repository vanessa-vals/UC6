#laço de repetição
#metodo para manipular lista
#lista

lista_compra = []

for i in range(3):
#for = para/ i= acrescentar/ in=na contagem /range=até 3 

    item = input("Digite o item:")
#item = chave/ input= escreva/ "digite o item"=texto que desejo que apresente 

    lista_compra.append(item)
#lista de compra = o que foi digitado/ iappend= vai acresentando o ultimo digitado

    print("Sua lista de compras")
 #print = apresentar o texto que deseja que apresente 

for valor in lista_compra:
 #for = para / valor= nova variavel /in=na contagem /losta de compra = resultado do lista_compra.append(item) 

    print("-", valor)
 #print = apresentar o texto que deseja que apresente / "-" = para deixar bonito / valor = nova variavel



 lista_nome = []

for i in range(4):

    lista = input("Digite um nome:")

    lista_nome.append(item)

remover = print("Escolha um nome para ser removido")

lista_nome = ["Ana", "Carlos", "Beatriz"]

if remover in lista_nome:
    lista_nome.remove(remover)
    print(f"{remover} foi removido com sucesso.")
else:
    print("Nome não encontrado")