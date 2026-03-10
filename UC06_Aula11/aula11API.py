import requests
 
#API
url = "https://rickandmortyapi.com/api/character"
 
resposta = requests.get(url) #Retorno status 200
 
# print(resposta)
json = resposta.json()
print(json)
 
personagem = json["results"] #Consulta os meus personagens
print(personagem)
 
#Excercicio 1
# laço de repetição para consultar apenas os nomes dos personagens
for nome_personagem in personagem:
    print (nome_personagem["name"])

for mais_info in personagem:
    print("Nome: ", mais_info["name"])
    print("Status: ", mais_info["status"])
    print("Especie: ", mais_info["species"])
    print("------------------------------------")

#exercicio 2
# Pedir ao usuário um ID e retornar da API o personagem referente a esse id  

import requests  # importar a biblioteca!

id_personagem = input("Digite um número: ") # Digitar para procurar ID direto na URL

link_api = f"https://rickandmortyapi.com/api/character/{id_personagem}"# A URL correta para buscar o personagem específico 

resposta2 = requests.get(link_api) #criar variavel que chama a a biblioteca +link da api de consulta

json2 = resposta2.json()# nome da variavel + json() é um MÉTODO, precisa dos parênteses ()

#print das informaçoes que desejo
print("Nome: ", json2["name"])
print("Status: ", json2["status"])
print("Especie: ", json2["species"])
print("------------------------------------")

