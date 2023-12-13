from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import mysql.connector
import json

app = Flask(__name__, template_folder='templates')
CORS(app)

def get_db_config():
    # Carregar informações do arquivo JSON
    with open('config.json', 'r') as file:
        config_data = json.load(file)

    return config_data.get('database', {})

# -----------------------------------------------------------------------------

@app.route('/todo/login/', methods=['POST'])
def login():
    # Captura das informações
    user = request.form.get('user')
    password = request.form.get('pass')

    # Carregar informações do arquivo JSON
    db_config = get_db_config()

    mydb = mysql.connector.connect(**db_config)

    try:
        # Inserir ao banco de dados
        mycursor = mydb.cursor()
        sql = "INSERT INTO tblogin (user, password) VALUES (%s, %s)"
        val = (str(user), str(password))
        mycursor.execute(sql, val)

        mydb.commit()
        response = {"user": str(user), "pass": str(password)}
    except ValueError:
        response = {"error": "Erro ao inserir no banco de dados"}

    return jsonify(response)

# ---------------------------------------------------------------------------------------------------------------

def fetch_cronograma_from_db():
    # Carregar informações do arquivo JSON
    db_config = get_db_config()

    mydb = mysql.connector.connect(**db_config)

    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM tbCronograma") 

    result = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return result

@app.route('/todo/cronograma/', methods=['POST'])
def cronograma():
    # Buscar informações do banco de dados
    cronograma_data = fetch_cronograma_from_db()

    # Formatar os dados para resposta ao usuário
    response = [{"data": item["data"], "motivo": item["motivo"], "local": item["local"]} for item in cronograma_data]

    return jsonify(response)
