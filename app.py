from flask import Flask, render_template,jsonify,json
import pyodbc
import requests

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

#   ====================================================

try:
    conn,cursor = connect_database()
    print("Conexão Realizada Com Sucesso!!")

except Exception as e:
    print("Falha na Conexão",e)
    exit()

finally:
    conn.close()

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

@app.route("/api/mapa",methods=['GET'])
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
    












if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)



