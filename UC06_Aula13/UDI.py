import pymysql as pySQL

# Arquivo para trabalhar com banco de dados e fazer as operacoes UPDATE, INSERT E DELETE

# CONEXAO COM O BANCO DE DADOS
conexao = pySQL.connect(
    host="localhost",         # endereço do servidor (local = "localhost")
    user="root",              # usuário do MySQL
    password="",              # senha do MySQL
    database="bd_livrariaonline",      # banco que você já criou
    port=3306                 # porta padrão do MySQL (opcional)
)

# Cria o cursor — versão dicionário (retorna {"coluna": valor})
cursor = conexao.cursor(pySQL.cursors.DictCursor)

try:
    # ── INSERT: adicionar um novo registro ──────
    # sql_insert = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
    # cursor.execute(sql_insert, ("Ana Santos", "anamaria@email.com"))
    # conexao.commit()  # ← confirma o INSERT
    # print("Inserido com sucesso! ID:", cursor.lastrowid)
    # # lastrowid -> RETORNAR O ID QUE FOI CRIADO

    # ── UPDATE: atualizar um registro existente ─
    # sql_update = "UPDATE clientes SET email = %s WHERE id_cliente = %s"
    # cursor.execute(sql_update, ("mesmo@email.com", 1))
    # conexao.commit()  # ← confirma o UPDATE
    # print("Linhas afetadas:", cursor.rowcount)

    # ── DELETE: remover um registro ─────────────
    cursor.execute("DELETE FROM compras WHERE id_compra = %s", (7,))
    conexao.commit()  # ← confirma o DELETE
    print("Linhas afetadas:", cursor.rowcount)

except Exception as erro:
    conexao.rollback()  # ← desfaz tudo se algo deu errado
    print("Erro! Operação revertida:", erro)
finally:
    cursor.close()
    conexao.close() # -> fechar a conexao com o banco de dados