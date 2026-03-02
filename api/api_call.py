from flask import Blueprint,jsonify,request,session
import requests

from database.projeto_mapa import connect_database
from secure.secure_routes import loguin_required
from util.validar_senha import criptograpy_senha,validar_senha

api_bp = Blueprint('api',__name__,template_folder='templates')

@api_bp.route("/api/get/mapa",methods=['GET'])
@loguin_required
def api_mapa():
    try:
        loc = []
        conn = connect_database()
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

@api_bp.route("/api/post/login",methods=['POST'])
def api_post_login():
    try:
        dados = request.get_json()
        email = dados.get('email')
        pwd = dados.get('pwd')

        conn = connect_database()
        cursor = conn.cursor()
        query = 'select senha,id from login where email =%s'
        cursor.execute(query,(email,))
        row = cursor.fetchone()
        
        if row is None or validar_senha(row[0],pwd) == False:#aq
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

@api_bp.route('/api/post/create/login',methods=['POST'])
def try_create_login():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    pwd = dados.get('pwd')
    pwd_encrypited = criptograpy_senha(pwd)

    try:
        conn = connect_database()
        cursor = conn.cursor()
        query = 'insert into login (nome,email,senha) values (%s,%s,%s)'
        cursor.execute(query,(nome,email,pwd_encrypited))
        conn.commit()
        print("Commit realizado")
        return jsonify({'Status':'Ok'})

        
    except Exception as e:
        return jsonify({"Erro":str(e)},500)

    finally:
        if 'conn' in locals():
            conn.close()
            

@api_bp.route("/api/check-auth")
def verify_login():
    if not session:
        return jsonify({"error": "not authenticated"})
    else:
        return jsonify({'Ok':'Login'})





        