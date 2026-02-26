from flask import Flask, render_template,jsonify, request
import pyodbc
import requests
import re

app = Flask(__name__)

#   === CONEXÃO COM O BANCO DE DADOS   ===  

def connect_database():
    conn = pyodbc.connect(
    'DRIVER={MySQL ODBC 9.4 ANSI Driver};'
    'SERVER=localhost;'
    'DATABASE=projeto_mapa;'
    'UID=root;'
    'PWD=1234;'
    )
    cursor = conn.cursor()
    return conn,cursor

try:
    conn,cursor = connect_database()
    print("Conexão Realizada Com Sucesso!!")

except Exception as e:
    print("Falha na Conexão",e)
    exit()

finally:
    conn.close()
#   ====================================================

#   === TRATANDO DADOS  ===
def validar_email(email):
    email = str(email).replace(" ",'')
        # Regex simples para validar formato de e-mail
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    return False










#   === DECLARANDO ROTAS === 

@app.route('/')
def login():
    return render_template('login.html')

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')















#   === API CALL ===

@app.route("/api/get/mapa",methods=['GET'])
def api_mapa():
    try:
        loc = []
        conn,cursor = connect_database()
        cursor = conn.cursor()
        query = 'select longitude_x, latitude_y, titulo from criar_denuncia'
        cursor.execute(query)
        row = cursor.fetchall()
        for i in row:
            ponto = {
                "longitude":i[0],
                "latitude":i[1],
                "titulo":i[2]
            }
            loc.append(ponto)
    finally:
        conn.close()
    return jsonify(loc)

@app.route('/api/cep/<cep>',methods=['GET'])
def carregar_cep(cep):
    cep = str(cep).replace("-",'').strip()
    json_cep = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return jsonify(json_cep)
    
@app.route("/api/post/login",methods=['POST'])
def api_post_login():
    try:
        dados = request.get_json()
        email = dados.get('email')
        pwd = dados.get('pwd')

        conn,cursor = connect_database()
        cursor = conn.cursor()
        query = 'select senha from login where email =?'
        cursor.execute(query,(email,))
        row = cursor.fetchone()
        if row and row[0] == pwd:
            return jsonify({"status":"ok"})
        else:
            return jsonify({"status":"negado"})
    except Exception as e:
        return jsonify({'Erro':e})
    finally:
        print("Testando api")








if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)



