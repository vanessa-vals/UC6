########DESVIOS CONDICIONAIS#####


# a função faz com que a variavel que foi associada a input permita adicionar uma informação para que depois use a variavel no print, segue exemplo
nome = input("Digite o seu nome: ")
print("Seu nome é:" , nome)

# indenpendente do que você digitar, o input vai transformar aquilo em texto, mesmo se for número
"""
Devido a isso, teremos que passar a especificar o tipo que estou digitando, como nùmero ou texto, 
para que assim o código fique de acordo e apresente aquilo que é necessário exemplo: Int = inteiro // #float = decimais
"""

""" Exemplo de código errado abaixo sem a especificação do tipo
numeros = input("Digite um numero de 1 a 10")
soma = numeros + 10
print("soma")
"""

# Exemplo com a especificação do tipo CORRETA
numeros = int(input("Digite um numero de 1 a 10: "))
soma = numeros + 10
print(soma)

""" Exemplo de código errado abaixo sem a especificação do tipo
calculo_salario = input("Digite o seu salário: "))
soma_salario = calculo_salario*3.5
print(soma_salario)
"""

# Exemplo com a especificação do tipo CORRETA
calculo_salario = float(input("Digite o seu salário: "))
soma_salario = calculo_salario*3.5
print(soma_salario)

""" No python, o : chama uma identação (que nada mais é que o espaço da borda, caso contrário o python não entende)Abaixo um exemplo de erro
#idade = 16
#if idade >=18:
#print("A sua idade é:" , idade) #sem o espaço dá erro
"""

"""Abaixo um exemplo com a identação correta apresentando o espaço do print"""
idade = 16

if idade >= 18: #false por que a idade não é maior ou igual a 18
    print("A sua idade é:" , idade)


#vamos seguir com uma estrtutura condicional de multiplos retonos (if - else) *verdadeiro - falso
#IF E ELSE

valida_idade = int(input("Digite sua idade: "))
if valida_idade < 18:
    print("Você é menor de idade e precisa da presença dos pais")
else:
    print("VOcê é maior de idade, pode entrar!")

#vamos seguir com uma estrtutura condicional para multiplas condições (if - else - elif) *verdadeiro - falso - senão se
#IF , ELSE e ELIF

nota = int(input("Digite a nota do aluno:"))
nome_aluno = input("Digite o nome do aluno:")
if nota >= 9:
    print(f" O aluno {nome_aluno} está  Aprovado com a nota {nota}" )
elif nota >=7 and nota <=8:
    print(f" O aluno {nome_aluno} está  na Aprovado por conselho com a nota {nota}" )
else: 
    print(f" O aluno {nome_aluno} está  na Reprovado por conselho com a nota {nota}" )

#Se o usuário for menor de idade então ele precisa ter autorização
# Se o usuário for maior de idade então ele pecisa ter a altura minima

idade_cliente = int(input("Digite a idade do cliente:"))
altura_cliente = float(input("Digite a altura do cliente:"))
if idade_cliente <18:
    print(f"O cliente é menor de idade e não pode entrar no brinquedo")
else:
    if altura_cliente >=1.50:
        print("Você é maior de idade e tem a altura mínima para o brinquedo")
    else:
        print("Você mesmo sendo maior de idade, tem menos que 1.50 de altura e não pode ir no brinquedo")
   # print("Cliente maior de idade e não pode entrar no brinquedo")

#OPERADOR TENÁRIO#
#instrução equivalente ao if e else, vantagem de fazer a condição em unica linha de código

#condicional ternário#
idade_cliente = int(input("Digite a idade do cliente:"))
status = ("menor de idade") if idade_cliente <18 else print("maior de idade")
print(status)









