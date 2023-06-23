import pymysql

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                       user = 'user',
                       password = 'password',
                       database = 'database',
                       port = 3306)
    cur = conn.cursor()
    cur.execute('''UPDATE Recaudacion SET NDescargas = ('%s'), NStreams = ('%s'), Monto = ('%s'), IdPlataforma_Streaming = ('%s'), IdFonograma = ('%s') WHERE IdRecaudacion = ('%s')''' % (event['ndescargas'], event['nstreams'], event['monto'], event['plataforma'], event['fonograma'], event['Id_Recaudacion']))
    conn.commit()
    cur.close()
    conn.close()
