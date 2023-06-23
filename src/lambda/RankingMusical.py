import pymysql
import json

def lambda_handler(event, context):
    
    conn = pymysql.connect(host = 'host_url',
                           user = 'user',
                           password = 'password',
                           database = 'database',
                           port = 3306)
    
    cur = conn.cursor()
    cur.execute('''SELECT F.IdFonograma, R.Monto, I.Nombre, F.Titulo FROM Recaudacion R, Fonograma F, Interprete_Fonograma U, Interprete I WHERE R.IdFonograma = F.IdFonograma AND F.IdFonograma = U.IdFonograma AND U.IdInterprete = I.IdInterprete''')
    resultado = cur.fetchall()
    #print(resultado)
    
    lista = json.loads(json.dumps(resultado, default=str))
    #print(lista)
    
    monto = float(0)
    ranking = []
    ranking_final = []
    
    for i in lista:
        cancion = i[3]
        interprete = i[2]
        id = i[0]
        
        for j in lista:
            if(cancion == j[3]):
                monto = monto + float(j[1])
        
        if(ranking == []):
            ranking.append([id, cancion, interprete, monto])
    
        else:
            existe = 'no'
            for k in ranking:
                if(cancion == k[1]):
                    existe = 'si'
            if(existe == 'no'):
                ranking.append([id, cancion, interprete, monto])
    
        #print(cancion + " " + interprete + " " + str(monto))
        monto = float(0)

    #print(ranking)

    while len(ranking) > 0:
        max = 0
        numeral = 0
        for j in ranking:
            numeral = numeral + 1
            if(j[3] >= max):
                max = j[3]
                posicion = numeral
                monto = j[3]
                interprete = j[2]
                cancion = j[1]
                id = j[0]

        ranking_final.append([id, cancion, interprete, monto])
        ranking.pop(posicion - 1)

    #print(ranking_final)

    cur.close()
    conn.close()

    return json.dumps(ranking_final, default=str)
