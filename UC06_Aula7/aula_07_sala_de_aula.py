
#atividade1

nome = input("Digite o seu nome: ")
idade = input("Digite sua: ")
cidade = input("Digite sua cidade: ")

dicionário = {
   "nome" : nome ,
   "idade" : idade ,
   "cidade" : cidade
}

for chave, valor in dicionário.items(): 
    print(chave, ":", valor)
    

#atividade2
nome_aluno = input("Digite o nome do aluno: ")
nota1= int(input("Digite a primeira nota de 0 a 10:"))
nota2=  int(input("Digite a segunda nota 0 a 10:"))
nota3=  int(input("Digite a terceira nota:"))
nota4=  int(input("Digite a quarta nota:"))
nota5=  int(input("Digite a ultima nota:"))
   
resultado = (nota1+nota2+nota3+nota4+nota5)/5
print(f"{nome_aluno} sua média foi:", str (resultado))

