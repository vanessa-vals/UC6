#Criar algotitmo que leia dois numeros inteiros e verifique qual é maior e qual é o menos e imprima o resultado no terminal

numero1 = int(input("Digite um número:"))
numero2 = int(input("Digite um outro número:"))
if numero1 > numero2:
 print(f"O número {numero1} é maior que o número {numero2}")
else:
 print(f"O número {numero1} é menor que o {numero2}")         

#Crie um algoritmo onde o usuário digita um numero de 1 até 12 e retorne em tela qual é o mês correspondente a ele
mes = int(input("Digite um número de 1 a 12:"))
if mes == 1:
 print(f" O mês {mes} corresponde a Janeiro")
elif mes == 2:
 print(f" O mês {mes} corresponde a Fevereiro")
elif mes == 3:
 print(f" O mês {mes} corresponde a Março")
elif mes == 4:
 print(f" O mês {mes} corresponde a Abril")
elif mes == 5:
 print(f" O mês {mes} corresponde a Maio")
elif mes == 6:
 print(f" O mês {mes} corresponde a Junho")
elif mes == 7:
 print(f" O mês {mes} corresponde a Juho")
elif mes == 8:
 print(f" O mês {mes} corresponde a Agosto")
elif mes == 9:
 print(f" O mês {mes} corresponde a Setembro")
elif mes == 10:
 print(f" O mês {mes} corresponde a Outubro")
elif mes == 11:
 print(f" O mês {mes} corresponde a Novembro")
else:
 print(f" O mês {mes} corresponde a Dezembro")


#Crie um programa de python que receba um numero inteiro do usuário e determine : É par ou é ímpar?
#O programa deve exibir ma teça se o número é par ou impoar
#num1%2 = 0(par)
numero = int(input("Digite um número:"))
resultado = numero%2  
if resultado ==0:
 print(f" O número é par")
else:
 print(f" O número é ímpar")

