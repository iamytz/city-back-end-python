from flask import Flask

from api.api_call import api_bp
from routes.routes import index_bp
from util.security_key import security_key

app = Flask(__name__)
app.secret_key = security_key()


#   === DECLARANDO ROTAS === 

app.register_blueprint(index_bp)
app.register_blueprint(api_bp)







if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)



