# Criar um menu para selecao
# 1 - Consultar por ID
# 2 - Consultar por nome
# 3 - Lista de personagens

# se for opcao 1:
"""
    Pedir ao usuario para digitar um ID(Numero inteiro) e retornar de dentro da API o personagem referente ao ID digitado
    Retorne todas as informações sobre o personagem
"""

# Se selecionar a opcao 2:
"""
    Pedir ao usuario para digitar nome e retornar o resultado

    OBS de codigo: para percorrer o json e retornar o nome digitado.
"""
    # for personagem in dados["results"]:
    #     print(personagem["name"])



# Se selecionar a opcao 3:
# Retornar todos os personagens
# Lista das informações que deverão ser retornadas:
"""
"results": [
"id":
"name":
"status":
"species":
"gender":

"origin": {
    "name": "Earth (C-137)",
},
"location": {
    "name": "Citadel of Ricks",
},
"image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
"""

import requests

while True:
    print("\n--- MENU DE SELEÇÃO ---")
    print("1 - Consultar por ID")
    print("2 - Consultar por nome")
    print("3 - Lista de personagens")
    print("3- Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id_escolhido = input("Digite o ID do personagem: ")
        url = f"https://rickandmortyapi.com/api/character/{id_escolhido}"
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            mais_info1 = resposta.json()
            print(f"\n--- Personagem Encontrado pelo ID ---")
            print("Nome: ", mais_info1["name"])
            print("Status: ", mais_info1["status"])
            print("Especie: ",mais_info1["species"])
            print("Genero: ", mais_info1["gender"])
            print(f"Localização de origem: {mais_info1['origin']['name']}")
            print(f"Localização atual: {mais_info1['location']['name']}")
            print(f"Criado em : {mais_info1['created'][:10]}")
            print("------------------------------------")
        else:
            print("ID não encontrado!")

    elif opcao =="2":
        nome_busca = input("Digite o nome do personagem: ")
        url = f"https://rickandmortyapi.com/api/character/?name={nome_busca}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            for mais_info2 in dados["results"]:
             print(f"ID: {mais_info2['id']}")
             print("Nome: ", mais_info2["name"])
             print("Status: ", mais_info2["status"])
             print("Especie: ", mais_info2["species"])
             print("Genero: ", mais_info2["gender"])
             print(f"Criado em : {mais_info2['created'][:10]}")
             print(f"Imagem : {mais_info2['image']}")
             print("------------------------------------")
   
        else:
             print("Personagem não encontrado!")

    elif opcao == "3":
        url = "https://rickandmortyapi.com/api/character"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            personagens = dados["results"] 

            for mais_info3 in personagens:
                print(f"ID: {mais_info3['id']}")
                print(f"Nome: {mais_info3['name']}")
                print(f"Status: {mais_info3['status']}")
                print(f"Especie: {mais_info3['species']}")
                print(f"Genero: {mais_info3['gender']}")
                print(f"Localização de origem: {mais_info3['origin']['name']}")
                print(f"Localização atual: {mais_info3['location']['name']}")
                print(f"Imagem : {mais_info3['image']}")
                print("------------------------------------")
        else:
            print("Erro ao conectar com a API.")

    elif opcao == "0": 
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")

   


