import pymysql

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                       user = 'user',
                       password = 'password',
                       database = 'database',
                       port = 3306)
    cur = conn.cursor()
    cur.execute('''UPDATE Fonograma SET Titulo = ('%s'), Duracion = ('%s'), FechaCreacion = ('%s'), IdGenero = ('%s'), IdObra_Musical = ('%s') WHERE IdFonograma = ('%s')''' % (event['titulo'], event['duracion'], event['fechacreacion'], event['genero'], event['obramusical'], event['Id_Fonograma']))
    conn.commit()
    cur.execute('''UPDATE Interprete_Fonograma SET IdInterprete = ('%s') WHERE IdFonograma = ('%s')''' % (event['interprete'], event['Id_Fonograma']))
    conn.commit()
    cur.close()
    conn.close()
