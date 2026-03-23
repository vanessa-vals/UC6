import pymysql as pySQL
import pandas as pd

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

# ── Buscar todos os registros ───────────────
cursor.execute("SELECT * FROM clientes")
todos = cursor.fetchall()
# Monta a lista FORA do loop
base_dados = []

for cliente in todos:
    base_dados.append({
        "nome": cliente["nome"],
        "email":  cliente["email"]
    })
    print(base_dados)


excel = pd.DataFrame(base_dados)
excel.to_excel("Aula13\Teste.xlsx", index=False)
print("Ação Finalizada....")
cursor.close()
conexao.close()