import pymysql
import json

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                           user = 'user',
                           password = 'password',
                           database = 'database',
                           port = 3306)
    cur = conn.cursor()
    cur.execute('''SELECT F.IdFonograma, F.Titulo, F.Duracion, F.FechaCreacion, G.Nombre, F.IdObra_Musical, IdProductora FROM Fonograma F, Genero G WHERE F.IdGenero = G.IdGenero''')
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return json.dumps(resultado, default=str)
