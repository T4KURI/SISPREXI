import pymysql
import json

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                           user = 'user',
                           password = 'password',
                           database = 'database',
                           port = 3306)
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Obra_Musical''')
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return json.dumps(resultado, default=str)
