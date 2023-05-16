import couchdb
import sys
import os

if __name__ == "__main__":
    #user = os.environ['COUCHDB_USER']
    #password = os.environ['COUCHDB_PASSWORD']
    user = "admin"
    password = "admin"
    server = couchdb.Server("http://%s:%s@couchdb:5984/" % (user, password))
    dbname = "db-proyecto-as"
    if dbname in server:
        print('Base de datos db-proyecto-as ya existente:\n')
        db = server[dbname]
    else:
        print('Se crea la base de datos db-proyecto-as:\n')
        db = server.create(dbname)
    print("\nSe crea la coleccion Personas\n")
    print("\nAlmacenamos 3 personas en ella\n")
    persona1 = {
        'tipo' : 'Persona',
        'NomAp' : 'Lucas Abaitua'
    }
    persona2 = {
        'tipo' : 'Persona',
        'NomAp' : 'Unai Lopez'
    }
    persona3 = {
        'tipo' : 'Persona',
        'NomAp' : 'Luis Enrique'
    }
    db.save(persona1)
    db.save(persona2)
    db.save(persona3)
    mongo = {'selector':{'tipo':'Persona'}}
    print("\nLos elementos de la coleccion son: \n")
    for i in db.find(mongo):
        print("- "+i['NomAp'])
    print("\n")
    print('##### PARA VER COUCHDB CON LA BD DE FORMA VISUAL: #####\n')
    print('Acceder al navegador e introducir:\n')
    print('	http://admin:admin@localhost:5984/_utils\n')
    exit
