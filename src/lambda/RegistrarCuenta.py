import pymysql

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                       user = 'user',
                       password = 'password',
                       database = 'database',
                       port = 3306)
    cur = conn.cursor()
    cur.execute('''INSERT INTO Usuario(Nombre, Apellido, Correo, Contraseña, IdProductora) VALUES ('%s', '%s', '%s', '%s', '%s' )''' % (event['nombre'], event['apellido'], event['correo'], event['contraseña'], 1))
    conn.commit()
    cur.close()
    conn.close()
