# crie uma função que receba 5 notas de um aluno e calcule e retorne a média.
#crie uma função para receber a média do aluno e retorne se ele esta aprovado ou reprovado

notas = []


for i in range(5):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

def calculo_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def situacao(media):
    if media >= 6: 
        return "Aprovado"
    else:
        return "Reprovado"

media_final = calculo_media(notas)
status = situacao(media_final)

print(f"A média do aluno é: {media_final}")
print(f"Status: {status}")






