import pymysql
import json
import boto3
import json

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'url',
                       user = 'user',
                       password = 'password',
                       database = 'database',
                       port = 3306)
    cur = conn.cursor()
    cur.execute('''INSERT INTO Obra_Musical(Titulo, Tipo_Obra) VALUES ('%s', '%s')''' % (event['titulo'], event['tipoobra']))
    conn.commit()
    obra_musical = cur.lastrowid
    
    #AnalisisDeSentimiento
    
    s3 = boto3.client("s3")
    bucket = "letrasmusicales"
    key = event['titulo']+".txt"
    
    file = s3.get_object(Bucket = bucket, Key = key)
    contenido = str(file['Body'].read())
    
    comprehend = boto3.client("comprehend")
    response = comprehend.detect_sentiment(Text = contenido, LanguageCode = "es")
    
    lista = json.loads(json.dumps(response, default=str))
    
    if(lista["Sentiment"] == "POSITIVE"):
        cur.execute('''INSERT INTO Letra_Musical(Letra, IdObra_Musical, IdTipo_Sentimiento) VALUES ('%s', '%s', '%s')''' % (key, obra_musical, 1))
        conn.commit()
    
    if(lista["Sentiment"] == "NEGATIVE"):
        cur.execute('''INSERT INTO Letra_Musical(Letra, IdObra_Musical, IdTipo_Sentimiento) VALUES ('%s', '%s', '%s')''' % (key, obra_musical, 2))
        conn.commit()
    
    if(lista["Sentiment"] == "MIXED"):
        cur.execute('''INSERT INTO Letra_Musical(Letra, IdObra_Musical, IdTipo_Sentimiento) VALUES ('%s', '%s', '%s')''' % (key, obra_musical, 3))
        conn.commit()
    
    else:
        cur.execute('''INSERT INTO Letra_Musical(Letra, IdObra_Musical, IdTipo_Sentimiento) VALUES ('%s', '%s', '%s')''' % (key, obra_musical, 4))
        conn.commit()
        
    #print(lista["Sentiment"])
    
    cur.close()
    conn.close()
    return json.dumps(obra_musical, default=str)
