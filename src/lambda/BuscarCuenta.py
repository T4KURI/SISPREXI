import pymysql
import json

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'database-mysql.c3ecu4syhg5e.us-east-1.rds.amazonaws.com',
                           user = 'admin',
                           password = 'admin123',
                           database = 'PRY20220223',
                           port = 3306)
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Usuario WHERE IdUsuario = ('%s')''' % (event['Id_Cuenta']))
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return json.dumps(resultado, default=str)
