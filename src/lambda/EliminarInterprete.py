import pymysql

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                           user = 'user',
                           password = 'password',
                           database = 'database',
                           port = 3306)
    cur = conn.cursor()
    cur.execute('''DELETE FROM Perfil WHERE IdInterprete = ('%s')''' % (event['Id']))
    conn.commit()
    cur.execute('''DELETE FROM Interprete WHERE IdInterprete = ('%s')''' % (event['Id']))
    conn.commit()
    cur.close()
    conn.close()
