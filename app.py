from flask import *
import pyodbc
from flask_ngrok import run_with_ngrok

from flask_restful import Resource ,Api

app=Flask(__name__)
api = Api(app)
run_with_ngrok(app)


#in SERVER, you have to write your own sql server name 
#in database, your database's name, obviously 
#in UID, your user in sql server, mine in sa for example
#in PWD, you should write your password 
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=**;DATABASE=**;UID=**;PWD=**;')
cursor = conn.cursor()

def dict_factory(cursor , data):
    results = []

    columns = [column[0] for column in cursor.description]

    for row in data:
        results.append(dict(zip(columns,row)))
    return jsonify(results)
    

class Inicio (Resource):
    def get(self):
        return jsonify({'Message ':'Home Page, you did it well :)'})

class clientes(Resource):
    def get(self):
        
        data = cursor.execute("SELECT * FROM clientes").fetchall()
        return dict_factory(cursor,data)
        
class Factura(Resource):
    def get(self):
        
        data = cursor.execute("SELECT * FROM factura ").fetchall()
        return dict_factory(cursor,data)




@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Something went wrong, check it out.</p>", 404


api.add_resource(clientes,'/api/clientes')
api.add_resource(Factura,'/api/facturas')
api.add_resource(Inicio,'/')


if __name__ =="__main__":
    app.run()


