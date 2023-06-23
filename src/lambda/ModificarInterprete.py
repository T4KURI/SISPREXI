import pymysql

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                       user = 'user',
                       password = 'password',
                       database = 'database',
                       port = 3306)
    cur = conn.cursor()
    cur.execute('''UPDATE Interprete SET Nombre = ('%s'), FechaDebut = ('%s'), FechaNacimiento = ('%s') WHERE IdInterprete = ('%s')''' % (event['nombre'], event['fechadebut'], event['fechanacimiento'], event['Id_Interprete']))
    conn.commit()
    cur.execute('''UPDATE Perfil SET URL = ('%s') WHERE IdRed_Social = ('%s') AND IdInterprete = ('%s')''' % (event['twitter'], 1, event['Id_Interprete']))
    conn.commit()
    cur.execute('''UPDATE Perfil SET URL = ('%s') WHERE IdRed_Social = ('%s') AND IdInterprete = ('%s')''' % (event['facebook'], 2, event['Id_Interprete']))
    conn.commit()
    cur.execute('''UPDATE Perfil SET URL = ('%s') WHERE IdRed_Social = ('%s') AND IdInterprete = ('%s')''' % (event['instagram'], 3, event['Id_Interprete']))
    conn.commit()
    cur.execute('''UPDATE Perfil SET URL = ('%s') WHERE IdRed_Social = ('%s') AND IdInterprete = ('%s')''' % (event['youtube'], 4, event['Id_Interprete']))
    conn.commit()
    cur.execute('''UPDATE Perfil SET URL = ('%s') WHERE IdRed_Social = ('%s') AND IdInterprete = ('%s')''' % (event['tiktok'], 5, event['Id_Interprete']))
    conn.commit()
    cur.close()
    conn.close()
