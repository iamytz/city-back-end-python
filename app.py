from flask import Flask

from api.api_call import api_bp
from routes.routes import index_bp
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # gera uma chave aleatória de 32 caracteres hexadecimais 


#   === DECLARANDO ROTAS === 

app.register_blueprint(index_bp)
app.register_blueprint(api_bp)







if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)



