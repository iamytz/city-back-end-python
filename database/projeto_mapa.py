import pymysql

#   === CONEXÃO COM O BANCO DE DADOS   === 

def connect_database():
    conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='projeto_mapa',
    charset='utf8mb4'
    )
    
    return conn

try:
    conn = connect_database()
    print("Conexão Realizada Com Sucesso!!")

except Exception as e:
    print("Falha na Conexão",e)
    exit()

finally:
    conn.close()