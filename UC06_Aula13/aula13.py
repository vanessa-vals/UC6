import pymysql as pySQL

conexao = pySQL.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "bd_livrariaonline",
  port = 3306
)
  
cursor = conexao.cursor(pySQL.cursors.DictCursor)

# buscar todos os registros
cursor.execute("SELECT *FROM clientes")
todos = cursor.fetchall() #o fetchall converte de SQL para python


print("-----------------------------------------Dados dos clientes----------------------------------------------------------------")
for cliente in todos:
    print(cliente["nome"],"-", cliente["email"],"-",  cliente["telefone"],"-",  cliente["data_cadastro"])

print("-----------------------------------------Dados das compras------------------------------------------------------------------")

cursor.execute("SELECT *FROM compras")
todos1 = cursor.fetchall()
for compras in todos1:
    print(compras["id_compra"],"-",  compras["id_cliente"],"-",  compras["id_livro"],"-",  compras["qtde"],"-",  compras["valor"],"-",  compras["desconto"],"-",  compras["data_compra"])

print("-----------------------------------------Dados das editoras------------------------------------------------------------------")

cursor.execute("SELECT *FROM editoras")
todos2 = cursor.fetchall()
for editoras in todos2:
    print(editoras["id_editora"],"-", editoras["nome"],"-",  editoras["email"],"-",  editoras["telefone"], "-", editoras["data_cadastro"])


# Buscar unico registro a partir do id sendo unico
cursor.execute("SELECT *FROM clientes WHERE id_cliente = 1")
cliente = cursor.fetchone()
print(cliente)

# vim cliente especifico
nome_busca = "Ursula Souza"
cursor.execute("SELECT *FROM clientes WHERE nome = %s",(nome_busca))
resultado = cursor.fetchall()
print(resultado)

# vim todas as vezes o nome citado com comando LIKE
nome_busca = "Ursula%"
cursor.execute("SELECT *FROM clientes WHERE nome LIKE %s",(nome_busca))
resultado = cursor.fetchall()
print(resultado)





   
 

