import sqlite3
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('template.html')  # Alterado para render_template, Flask usa HTML

@app.route('/line')
def dashboard_line():
    return render_template('template_line.html')  # Alterado para render_template, Flask usa HTML

@app.route('/gauge')
def dashboard_gauge():
    return render_template('template_gauge.html')  # Alterado para render_template, Flask usa HTML


@app.route('/get_latest_value')
def get_latest_value():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Query the database to get the latest value and timestamp
    cursor.execute('SELECT value, timestamp FROM NIVEL ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    
    conn.close()
    
    value = result[0] if result else "N/A"
    timestamp = result[1] if result else "N/A"
    
    return jsonify({'value': value, 'timestamp': timestamp})  # Flask usa jsonify para respostas JSON

if __name__ == '__main__':
    app.run(host='localhost', port=8090)
