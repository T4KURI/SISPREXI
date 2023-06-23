import pymysql
import json

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                       user = 'user',
                       password = 'password',
                       database = 'database',
                       port = 3306)
    cur = conn.cursor()
    cur.execute('''INSERT INTO Obra_Musical(Titulo, Tipo_Obra) VALUES ('%s', '%s')''' % (event['titulo'], event['tipoobra']))
    conn.commit()
    obra_musical = cur.lastrowid
    cur.execute('''INSERT INTO Letra_Musical(Letra, IdObra_Musical, IdTipo_Sentimiento) VALUES ('%s', '%s', '%s')''' % (event['titulo'], obra_musical, 2))
    conn.commit()
    cur.close()
    conn.close()
    return json.dumps(obra_musical, default=str)
