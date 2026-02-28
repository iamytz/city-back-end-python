from flask import Flask

from api.index import api_bp
from routes.index import index_bp

app = Flask(__name__)
app.secret_key = 'qualquer_coisa_super_secreta'

 


#   === DECLARANDO ROTAS === 

app.register_blueprint(index_bp)
app.register_blueprint(api_bp)






if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)



