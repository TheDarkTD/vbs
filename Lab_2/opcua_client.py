import sqlite3
from datetime import datetime
from opcua import Client
from flask import Flask, render_template_string

# Endereço e porta do servidor OPC UA
opc_server_url = "opc.tcp://localhost:4840/freeopcua/server/"
# Nó da variável nível no servidor OPC UA
node_id = "ns=2;i=2"
# Nome do banco de dados SQLite
db_name = "pv_database.db"

app = Flask(__name__)

# Função que busca o valor da variável nível no servidor OPC UA e armazena no banco de dados
def get_nivel():
    # Conecta ao servidor OPC UA
    client = Client(opc_server_url)
    client.connect()
    node = client.get_node(node_id)
    nivel = node.get_value()
    client.disconnect()

    # Armazena o valor no banco de dados
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO nivel (timestamp, valor) VALUES (?, ?)", (timestamp, nivel))
    conn.commit()
    conn.close()

    return nivel

# Rota do servidor web que exibe o valor da variável nível em uma página HTML
@app.route('/')
def index():
    # Atualiza o valor da variável nível
    nivel = get_nivel()

    # Recupera o último valor da variável nível armazenado no banco de dados
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT valor FROM nivel ORDER BY timestamp DESC LIMIT 1")
    result = c.fetchone()
    if result:
        nivel_bd = result[0]
    else:
        nivel_bd = None
    conn.close()

    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Nível do Reservatório</title>
    </head>
    <body>
        <h1>Monitoramento do Nível do Reservatório</h1>
        <p><b>Nível atual:</b> {{nivel}}</p>
        <p><b>Nível anterior:</b> {{nivel_bd}}</p>
    </body>
    </html>
    '''

    return render_template_string(template, nivel=nivel, nivel_bd=nivel_bd)

if __name__ == '__main__':
    # Roda o servidor web na porta 8082
    app.run(host='localhost', port=8082)
