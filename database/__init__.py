import pyodbc

#   === CONEXÃO COM O BANCO DE DADOS   === 

def connect_database():
    conn = pyodbc.connect(
    'DRIVER={MySQL ODBC 9.4 ANSI Driver};'
    'SERVER=localhost;'
    'DATABASE=projeto_mapa;'
    'UID=root;'
    'PWD=1234;'
    )
    cursor = conn.cursor()
    return conn,cursor

try:
    conn,cursor = connect_database()
    print("Conexão Realizada Com Sucesso!!")

except Exception as e:
    print("Falha na Conexão",e)
    exit()

finally:
    conn.close()