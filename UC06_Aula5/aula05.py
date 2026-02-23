#Laços de repetição#
"""
São comandos para executar instruções mais de uma vez com um numero limitado de vezes
Possui variaveis de controle , e sempre é necessário teste qu vai resultar em uma condição de valor booleano (verdadeiro), 
que é cessado quando encontar o falso

Laço While - repete a instrução enquanto for verdadeira. Quando encontrar a condição falsa, a execução é interrompido 

A sintase while para uso: 

Exemplo: 
contador = 1
while contador <=5:
  print(contador)
  contador +=1

  contador = 1
while contador <=5:
  print(contador)
  contador +=1
"""
contador = 1
while contador <=5:
  print(contador)
  contador +=1
 
"""
  Cuidado com loop infinito
  while true:
   print("Loop infinito")
  """

"""
Laço For - não gera condição sem antes testar a condição
range é a condição funciona como maior ou igual
Exemplo:
contador2 = 
 for = contador2 in range(5)
 print()
contador2 <=16
para fazer um decremento ( tirar valor), pode utilizar 3 parametros, segue exemplo:
(17, 2, -3)
(considerar numero 17, até o numero 2, tirando sempre 3)
exemplo do ressultado:
17
14
11
8
5
2
"""

contador2 =20
for contador2 in range(5, 15):
   print(contador2)
