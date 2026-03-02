from werkzeug.security import generate_password_hash, check_password_hash

def criptograpy_senha(pwd):
    pwd = str(pwd)
    if len(pwd) <8:
        return False
    else:
        pwd_hash = generate_password_hash(pwd)
        return pwd_hash

def validar_senha(corret_pwd,pwd):
    pwd = str(pwd)
    if check_password_hash(corret_pwd,pwd) == False:
        return False
    else:
        return True
