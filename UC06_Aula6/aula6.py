""" para que apareça somente determinados caracteres de um texto cada caractere é considerado um numeral sempre iniciando por 0 exemplo
SENAC
01234
"""
texto1 = "SENAC"
print(texto1[0])
print(texto1[3])
print(texto1[-1])
 
"""
Caso eu coloque -numeral ele vem do final para o primeiro
"""

# FUNÇÃO len contabiliza quantidade de caracteres que tem no texto ()
texto2 = "Assim mesmo, o entendimento das metas propostas maximiza as possibilidades por conta do remanejamento dos quadros funcionais."
print(len(texto2))



#FUNÇÃO UPPER(TUDO MAIUSCULO),LOWER(TUDO MINUSCULO), CAPITALIZE(PRIMEIRA LETRA MAIUSCULA) E TITLE(PRIMEIRA DE CADA PALAVRA)
texto3 = "ola galerinha"
print(texto3.upper()) 
texto4 = "olA GALERINHa"
print(texto4.lower()) 
texto5 = "ola galerinha"
print(texto5.capitalize()) 
texto6 = "ola galerinha"
print(texto6.title()) 

"""
SUBSTRING
"""

# RETORNA PEQUENAS PARTES DO TEXTO ( SEMPRE POSICIONAR UMA POSIÇÃO ANTES)
texto7 = "Vanessa "
print(texto7[0:4]) #adicionando nesta forma vai apresentar somente VA que seria 0 e 1 , parando no 2 caractere
print(texto7[:2]) 
print(texto7[:3]) 

#REPLACE () É USADO QUANDO NECESSÁRIO FAZER A SUBSTITUIÇÃO DE UMA STRING POR OUTRA
texto8 = "Hoje é aula da Heloísa"
novo_texto = texto8.replace("da Heloísa", "do José")
print(novo_texto)


#REMOVER OS ESPAÇOS DA STRING adicionando strip , OU LADO +STRIP
texto9 = "   Olá Mundo         "
print(texto9.strip()+"String")#remove direito e esquerda
print(texto9.lstrip()+"String")#remove esquerda
print(texto9.rstrip()+"String")#remove direito 

#MÉTODO DE BUSCA EM STRINGS
"""
Usamos IN para retornar um texto boolleano em uma string
"""

texto10 = "Pulei carnaval, mas hoje estou estudando"
print ("carnaval" in texto10)
#case sensitive = sensivel letras maiusculas e minusculas

#encontrar texto especifico com find
print(texto10.find("estudando")) #aparece a posição
print(texto10[31]) #teste de confirmação da posição

#contar as ocorrências
print(texto10.count("a"))

#startswith e endswith buscar se o texto começa com determinadas caracteres e/ou termina com determinadas caracteres
texto11 = "Eu amo Java"
print(texto11.startswith("Eu"))
print(texto11.endswith("va"))
