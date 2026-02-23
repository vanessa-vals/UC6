numero_digitado = int(input("Digite um numero de 1 a 10:"))

if numero_digitado >=1 and numero_digitado <= 10:
   print("Tabuada do numero:" , (numero_digitado))

   for i in range(1, 11):
      resultado = numero_digitado * i
      print(F"{numero_digitado} x {i} = {resultado}")
else:
    print("Erro: O valor é inválido.")
 







