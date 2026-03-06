#função open para abrir um arquivo

"""
open("nome_do_arquivo.txt", "modo")"""

#classificação dos modos 
"""
"w" escreve (apaga tudo e escreve de novo) sobre escrevendo tudo
"a" adiciona conteúdo ao final como a função append de lista
"r" lê o arquivo
with= para que o arquivo seja fechado corretamente como se fosse um salvamento automatico enquanto percorro o código
as = como
"""

#criar caso o arquivo não exista
# open("nota.txt", "w")

#abrir e ou criar um arquivo e digitar informações
with open("nota.txt", "w") as nota_aluno:
    nota_aluno.write("Por conseguinte, a constante divulgação das informações assume importantes posições no estabelecimento das posturas dos órgãos dirigentes com relação às suas atribuições.")

# efetua a leitura do que foi adicionado
with open("nota.txt", "r") as leitura_arquivo:
   recebe_texto = leitura_arquivo.read()
   print(recebe_texto)

# adiciona mais informações ao final do arquivo
with open("nota.txt", "a") as adiciona_novo_texto:
   adiciona_novo_texto.write("\n Aqui tem uma nova linha de texto")






