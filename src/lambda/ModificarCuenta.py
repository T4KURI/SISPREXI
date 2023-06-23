import pymysql

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                       user = 'user',
                       password = 'password',
                       database = 'database',
                       port = 3306)
    cur = conn.cursor()
    cur.execute('''UPDATE Usuario SET Nombre = ('%s'), Apellido = ('%s'), Correo = ('%s'), Contraseña = ('%s') WHERE IdUsuario = ('%s')''' % (event['nombre'], event['apellido'], event['correo'], event['contraseña'], event['Id_Cuenta']))
    conn.commit()
    cur.close()
    conn.close()
