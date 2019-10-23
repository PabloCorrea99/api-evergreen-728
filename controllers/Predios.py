from flask import jsonify, request 
from db.db import cnx 

class Predio(): 
    global cur 
    cur = cnx.cursor()

    def list(): 
        lista = []
        cur.execute("SELECT * FROM predios")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows: 
            registro = zip(columns, row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close 

    def create(body): 
        data = (body['codigo'],body['area'],body['latitud'],body['longitud'],body['terreno'],body['imagen'])
        sql="INSERT INTO predios(codigo, area, latitud, longitud, terreno, imagen) VALUES(%s, %s, %s, %s, %s, %s)" 
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': "Insertado"}, 200