import pymysql
import json

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                           user = 'user',
                           password = 'password',
                           database = 'database',
                           port = 3306)
    cur = conn.cursor()
    cur.execute('''SELECT R.IdRecaudacion, R.NDescargas, R.NStreams, R.Monto, P.Nombre, F.Titulo FROM Recaudacion R, Plataforma_Streaming P, Fonograma F WHERE R.IdPlataforma_Streaming = P.IdPlataforma_Streaming AND R.IdFonograma = F.IdFonograma;''')
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return json.dumps(resultado, default=str)
