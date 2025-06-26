import sqlite3

# Cria a conexão com o banco de dados
conn = sqlite3.connect('pv_database.db')

# Cria a tabela 'NIVEL'
conn.execute('''CREATE TABLE NIVEL
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             valor REAL,
             timestamp INTEGER);''')

# Fecha a conexão
conn.close()
