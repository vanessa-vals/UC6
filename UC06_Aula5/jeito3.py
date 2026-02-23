numero = int(input("Digite um número para ver a tabuada: "))
 
if numero >= 0:
   
    for contador in range(0, 11):
        print(numero, "x", contador, "=", numero * contador)
       
else:
    print("Número inválido, tente novamente")