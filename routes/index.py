from flask import Blueprint,render_template
from secure.__init__ import loguin_required

index_bp= Blueprint('index',__name__,template_folder='templates')

@index_bp.route('/')
def login():
    return render_template('login.html')

@index_bp.route("/index")
@loguin_required
def index():
    return render_template("index.html")

@index_bp.route('/mapa')
@loguin_required
def mapa():
    return render_template('mapa.html')