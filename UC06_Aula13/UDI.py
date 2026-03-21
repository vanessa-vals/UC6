import pymysql as pySQL

# arquivo para trabalhar com banco de dados e fazer as operações UPDATE, INSERT E DELETE

conexao = pySQL.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "bd_livrariaonline",
  port = 3306
)
  
cursor = conexao.cursor(pySQL.cursors.DictCursor)

try:#"tentar" executar um bloco de código que você suspeita que pode dar erro
     sql_insert ="iNSERT INTO clientes (nome, email) VALUES (%s, %s)" #manter a segurança da query para passar os paramentros atravès da %S
     cursor.execute(sql_insert, ("Ana Lima","ana@email.com"))
     conexao.commit() #confirmar inserção
     print("Inserido com sucesso! ID:", cursor.lastrowid) #lastrowid= descobrir qual foi o ID gerado automaticamente na última inserção que você fez.
except Exception as erro: #Aqui você define o que o Python deve fazer se o erro acontecer.
     conexao.rollback() #desfaz o que deu errado
     print("Erro!Operação revertida:" , erro)
finally: #finaliza a conexão após ela ser realizada
     cursor.close()
     conexao.close()


try:
# UPDATE: ATUALIZAR REGISTRO EXISTENTE
    sql_update = "UPDATE clientes SET email = %s WHERE id_cliente = %s"
    cursor.execute(sql_update, ("novo@rmail", 1))
    conexao.commit() #confirma o UPDATE
    print("Linhas afetadas:" , cursor.rowcount) #rowcount = linhas alteradas

#DELETE: remover um registro
    cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (5))
    conexao.commit() #confirma o DELETE
    


except Exception as erro: #Aqui você define o que o Python deve fazer se o erro acontecer.
    conexao.rollback() #desfaz o que deu errado
    print("Erro!Operação revertida:" , erro)
finally: #finaliza a conexão após ela ser realizada
    cursor.close()
    conexao.close()


