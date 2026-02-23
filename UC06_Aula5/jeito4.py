numero = int(input("Digite um número: "))
 
while numero < 0:
    print("Número inválido, tente novamente")
    numero = int(input("Digite um número: "))
 
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)