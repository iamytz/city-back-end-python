from flask import jsonify,session
from functools import wraps

def loguin_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if "id" not in session:
            return jsonify({"error": "not authenticated"}), 401
        return f(*args,**kwargs)
    return decorated_function