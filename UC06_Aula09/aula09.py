"""
#para python entender função chamar a palavra def

"""
# def nome_da_função(parametros):
    #código
    # return resultado

    # Exemplo: 
"""

def saudacao():
    print("Olá, seja bem-vinda")
saudacao()

#quando criamos um código fora da função é considerado uma variavel global
nome ="Beltrano"

#parametros sempre vão dentro do parenteses
def saudacao():
    print("Olá,", nome, " seja bem-vinda")

#chama a função
saudacao()

#funções podem retonar valores usando return
def somar(a, b):
 return a + b
resultado = somar(5, 3)
print(resultado)
"""

#recebe dois valores, faz a soma e retorna o resultado

def soma(valor1, valor2):
   return valor1 + valor2

salario_funcionario = 1600
beneficio = 200
novo_salario = soma(salario_funcionario, beneficio)
print(novo_salario)

#soma dois valores se a idade do usuário for igual ou maior do que 18
#senaõ mostra mensagem "Sua idade é menor que 18"

idade_usuario = int(input("Digite sua idade: "))
if idade_usuario >=18:
   var1 = int(input("Digite o primeiro valor: "))
   var2 = int(input("Digite o segundo valor: "))
   resultado = soma (var1, var2)
   print(resultado)
else :
 print("Sua idade é menor que 18")

 #função retorna a quantidade de itens de uma lista e também funciona com strings(strings = texto)
 lista = [20, 1, 6, 10, 45]
 palavra = "Ano"

#retornar a quantidade de itens da lista
print(len(lista))
print(len(palavra))

#função sum soma valores de lista numerica
print("A soma da lista é",sum(lista))

#função max e min ( maior e menor valor)
print("Máximo",max(lista))
print("Mínimo", min(lista))

#função para ordenar os numeros com função sorted
print(sorted(lista))

#O type Retorna o tipo de valor que foi adicionado na variavel
tipo = 10.90
print(type(tipo))

#converter tipos (exemplo, inteito para str, float para int, booleano para str) built - in
print(float(tipo))
print(int(tipo))

   


