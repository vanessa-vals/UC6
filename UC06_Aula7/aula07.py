
#Dicionário em python são estruturas que guardam dados em formato chave e guarda uma sequencia de dados de uma única vez
"""
A Estrutura Chave-Valor
Um dicionário é composto por pares de chave: valor.
Chave: É o identificador (como o nome de uma pessoa).
Valor: É o dado guardado (como o número do telefone).

chave = {
    "nome da pessoa": "número do telefone",
    }
"""

aluno = {
"nome" : "Ana",
"idade" : 14, 
"nota" : 8.5 ,
"curso" : "Técnico de Informatica para internet" ,
"Array" : [30, True, "Texto"] ,
"endereco" : {
    "Rua" : "Rua dois" ,
    "Cidade" : "Santo André" ,
    "estado" : "SP" ,
}
}
#Array (veremos na aula sexta [30, True, "Texto"])

print(aluno["nome"])
print(aluno["Array"])
#cessar dentro de um outro dicionário
print(aluno["endereco"])
#acessar apenas um unico dado do endereço
print(aluno["endereco"]["estado"])
#acessar campo especifico do array escolhe a posição lembrando a regra que o primeiro é 0(sempre escolher -1 posição)
print(aluno["Array"][2])

#como alterar os dados do dicionário
aluno["idade"] = 20
print(aluno["idade"])

#alterar a informação do array que esta dentro do dicionário com uma informação e posição especifica
aluno["Array"][2] = 9
print(aluno["Array"][2])

#alterar um dado que está dentro do dicionário que está dentro do dicionário endereço
#sempre que precisar acessar uma chave dentro de um dicionário usar []
#se precisa acessar campo especifico [][]
#no dicionario ão se usa () somente quando for chamar ele no print
aluno["endereco"]["cidade"] = "São Paulo"
print(aluno["endereco"])
print(aluno)

#adicionar novo campo vinculada a chave sem precisar mexer na chave original
aluno["periodo"] = "Noturno"
print(aluno)

#criar, ler, alterar e deletar
#comando del para deletar a informação
del aluno["idade"] , aluno["curso"]
print(aluno)


"""
for item in sequencia:
    # Código a ser executado para cada item
for: Inicia o laço (loop). Significa "Para cada...".

item: É uma variável que você cria na hora. Ela vai "segurar" o valor do elemento atual da repetição.

in: Indica de onde você está tirando esses itens. Significa "... dentro de...".

sequencia: É o conjunto de dados que você quer explorar (uma lista de nomes, um texto, etc.)."""

#percorrer um dicionário usando laço de repetição para resultar o nome da chave
for chave in aluno: 
    print(chave)

#percorrer um dicionário usando laço para resultar a informação da chave usando valor e chave+.values geral
for valor in aluno.values(): 
    print(valor)

#percorrer um dicionário e retornar a chave de um valor usando laço organizando as informações
for chave, valor in aluno.items(): 
    print(chave, ":", valor)

