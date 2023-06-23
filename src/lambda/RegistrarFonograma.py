import pymysql

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                       user = 'user',
                       password = 'password',
                       database = 'database',
                       port = 3306)
    cur = conn.cursor()
    cur.execute('''INSERT INTO Fonograma(Titulo, Duracion, FechaCreacion, IdGenero, IdObra_Musical, IdProductora) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')''' % (event['titulo'], event['duracion'], event['fechacreacion'], event['genero'], event['obramusical'], 1))
    conn.commit()
    fonograma = cur.lastrowid
    cur.execute('''INSERT INTO Interprete_Fonograma(IdInterprete, IdFonograma) VALUES ('%s', '%s')''' % (event['interprete'], fonograma))
    conn.commit()
    cur.close()
    conn.close()
