from flask import Flask, render_template,jsonify, request, session
import pyodbc
import requests
import re
from functools import wraps


app = Flask(__name__)
app.secret_key = 'qualquer_coisa_super_secreta'

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

#   === ARMAZENANDO DEFS  ===
def validar_email(email):
    email = str(email).replace(" ",'')
        # Regex simples para validar formato de e-mail
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    return False

def loguin_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if "id" not in session:
            return jsonify({"error": "not authenticated"}), 401
        return f(*args,**kwargs)
    return decorated_function







#   === DECLARANDO ROTAS === 

@app.route('/')
def login():
    return render_template('login.html')

@app.route("/index")
@loguin_required
def index():
    return render_template("index.html")

@app.route('/mapa')
@loguin_required
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
@loguin_required

@app.route('/api/cep/<cep>',methods=['GET'])
@loguin_required
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
        query = 'select senha,id,nome from login where email =?'
        cursor.execute(query,(email,))
        row = cursor.fetchone()
        if row is None or row[0] != pwd:
            return jsonify({
                "status": "error",
                "message": "Invalid credentials"
                })          
        else:
            session['id'] = row[1]
            return jsonify({
                "status": "success",
                "message": "Login accepted"
                })

    except Exception as e:
        return jsonify({'Erro':e})
    finally:
        conn.close()
        print("Testando api")




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)



