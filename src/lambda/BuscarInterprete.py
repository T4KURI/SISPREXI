import pymysql
import json

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                           user = 'user',
                           password = 'password',
                           database = 'database',
                           port = 3306)
    cur = conn.cursor()

    if(event['Metodo'] == '1'):

        cur.execute('''SELECT * FROM Interprete WHERE IdInterprete = ('%s')''' % (event['Id_Interprete']))
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return json.dumps(resultado, default=str)

    if(event['Metodo'] == '2'):
        cur.execute('''SELECT * FROM Perfil WHERE IdInterprete = ('%s')''' % (event['Id_Interprete']))
        resultado = cur.fetchall()
        cur.close()
        conn.close()
        return json.dumps(resultado, default=str)
