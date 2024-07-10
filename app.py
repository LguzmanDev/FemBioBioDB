from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import psycopg2
import os
from urllib.parse import quote_plus

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def url_quote(s):
    if isinstance(s, str):
        s = s.encode("utf-8")
    return quote_plus(s)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM emprendimiento')
    emprendimientos = cursor.fetchall()
    print(emprendimientos)  # Esto imprimirá los datos en la consola
    cursor.close()
    conn.close()
    return render_template('index.html', emprendimientos=emprendimientos)

@app.route('/profile/<run>')
def profile(run):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Obtener datos del emprendimiento
    cursor.execute('SELECT * FROM emprendimiento WHERE run = %s', (run,))
    emprendimiento = cursor.fetchone()
    
    # Obtener datos del detalle basado en el id del emprendimiento
    if emprendimiento:
        cursor.execute('SELECT * FROM detalle WHERE id = %s', (emprendimiento[0],))
        detalle = cursor.fetchone()
    else:
        detalle = None
    
    cursor.close()
    conn.close()
    
    return render_template('profile.html', emprendimiento=emprendimiento, detalle=detalle)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
