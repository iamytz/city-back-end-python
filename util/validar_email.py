import re
def validar_email(email):
    email = str(email).replace(" ",'')
        # Regex simples para validar formato de e-mail
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(padrao, email):
        return True
    return False