import pymysql

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                           user = 'user',
                           password = 'password',
                           database = 'database',
                           port = 3306)
    cur = conn.cursor()
    cur.execute('''DELETE FROM Recaudacion WHERE IdFonograma = ANY (
        SELECT IdFonograma FROM Fonograma WHERE IdObra_Musical = ('%s'))''' % (event['Id']))
    conn.commit()
    cur.execute('''DELETE FROM Interprete_Fonograma WHERE IdFonograma = ANY (
        SELECT IdFonograma FROM Fonograma WHERE IdObra_Musical = ('%s'))''' % (event['Id']))
    conn.commit()
    cur.execute('''DELETE FROM Fonograma WHERE IdObra_Musical = ('%s')''' % (event['Id']))
    conn.commit()
    cur.execute('''DELETE FROM Letra_Musical WHERE IdObra_Musical = ('%s')''' % (event['Id']))
    conn.commit()
    cur.execute('''DELETE FROM Obra_Musical WHERE IdObra_Musical = ('%s')''' % (event['Id']))
    conn.commit()
    cur.close()
    conn.close()
