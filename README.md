# Flask simple RESTapi 

This was an university homework I had to made.
This is a simple api who reads data from sql server database and return it as a json format and then is consumed by an android application in android studio

## Installation
Install virtualenv with pip
```bash
pip install virtualenv
```

Create a virtual environment in your work folder.
```bash
virtualenv virtual
```

Use [pip](https://pip.pypa.io/en/stable/) to install the dependencies written in requirements.txt.

```bash
pip install -r requirements.txt
```

## Edit the connection to sql Server

```python
#in SERVER, you have to write your own sql server name 
#in database, your database's name, obviously 
#in UID, your user in sql server, mine in sa for example
#in PWD, you should write your password 
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=***;DATABASE=***;UID=***;PWD=***')
```
## Edit the methods

```python

class Inicio (Resource):
    def get(self):
        return jsonify({'Message ':'Home Page, you did it well :)'})

class clientes(Resource):
    def get(self):
        
        data = cursor.execute("SELECT * FROM (your table name)").fetchall()
        return dict_factory(cursor,data)
        
class Factura(Resource):
    def get(self):
        
        data = cursor.execute("SELECT * FROM (your table name again) ").fetchall()
        return dict_factory(cursor,data)
```

## Edit the path

```python
api.add_resource(clientes,'/api/(your path)')
api.add_resource(Factura,'/api/(your path)')
api.add_resource(Inicio,'/')

```
  

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Lets get in touch
[Text me](https://www.facebook.com/jose.rodriguessotela)

 
