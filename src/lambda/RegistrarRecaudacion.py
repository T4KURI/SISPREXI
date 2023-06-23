import pymysql

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                       user = 'user',
                       password = 'password',
                       database = 'database',
                       port = 3306)
    cur = conn.cursor()
    cur.execute('''INSERT INTO Recaudacion(NDescargas, NStreams, Monto, IdPlataforma_Streaming, IdFonograma) VALUES ('%s', '%s', '%s', '%s', '%s')''' % (event['ndescargas'], event['nstreams'], event['monto'], event['plataforma'], event['fonograma']))
    conn.commit()
    cur.close()
    conn.close()
