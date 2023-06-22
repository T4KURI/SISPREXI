import pymysql
import json

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
      user = 'user',
      password = 'password',
      database = 'database',
      port = 3306)
    cur = conn.cursor()
    cur.execute('''INSERT INTO Interprete(Nombre, FechaDebut, FechaNacimiento) VALUES ('%s', '%s', '%s')''' % (event['nombre'], event['fechadebut'], event['fechanacimiento']))
    conn.commit()
    interprete = cur.lastrowid
    cur.execute('''INSERT INTO Perfil(URL, IdRed_Social, IdInterprete) VALUES ('%s', '%s', '%s')''' % (event['twitter'], 1, interprete))
    conn.commit()
    cur.execute('''INSERT INTO Perfil(URL, IdRed_Social, IdInterprete) VALUES ('%s', '%s', '%s')''' % (event['facebook'], 2, interprete))
    conn.commit()
    cur.execute('''INSERT INTO Perfil(URL, IdRed_Social, IdInterprete) VALUES ('%s', '%s', '%s')''' % (event['instagram'], 3, interprete))
    conn.commit()
    cur.execute('''INSERT INTO Perfil(URL, IdRed_Social, IdInterprete) VALUES ('%s', '%s', '%s')''' % (event['youtube'], 4, interprete))
    conn.commit()
    cur.execute('''INSERT INTO Perfil(URL, IdRed_Social, IdInterprete) VALUES ('%s', '%s', '%s')''' % (event['tiktok'], 5, interprete))
    conn.commit()
    cur.close()
    conn.close()
    return json.dumps(interprete, default=str)