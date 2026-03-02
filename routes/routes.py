from flask import Blueprint,render_template
from secure.secure_routes import loguin_required

index_bp= Blueprint('index',__name__,template_folder='templates')

@index_bp.route('/')
def login():
    return render_template('index.html')

@index_bp.route("/login")

def index():
    return render_template("login.html")

@index_bp.route('/mapa')
@loguin_required
def mapa():
    return render_template('mapa.html')

@index_bp.route('/create/login')
def create_login():
    return render_template('create_login.html')


