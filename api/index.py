from flask import Blueprint,jsonify,request,session
import requests

from database.__init__ import connect_database
from secure.__init__ import loguin_required
api_bp = Blueprint('api',__name__,template_folder='templates')

@api_bp.route("/api/get/mapa",methods=['GET'])
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

@api_bp.route('/api/cep/<cep>',methods=['GET'])
@loguin_required
def carregar_cep(cep):
    cep = str(cep).replace("-",'').strip()
    json_cep = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return jsonify(json_cep)
    
@api_bp.route("/api/post/login",methods=['POST'])
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