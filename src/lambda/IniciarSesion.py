import pymysql
import json

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                           user = 'user',
                           password = 'password',
                           database = 'database',
                           port = 3306)
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Usuario WHERE Correo = ('%s') AND Contraseña = ('%s')''' % (event['correo'], event['contraseña']))
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return json.dumps(resultado, default=str)
