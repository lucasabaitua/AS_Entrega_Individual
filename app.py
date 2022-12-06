import couchdb
import sys

if __name__ == "__main__":  
    server = couchdb.Server("http://admin:admin@34.116.172.170:5984/")
    dbname = "db-proyecto-as"
    if dbname in server:
        db = server[dbname]
    else:
        db = server.create(dbname)
    print("\nSe crea la colección Personas\n")
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
    print("\nLos elementos de la colección son: \n")
    for i in db.find(mongo):
        print("- "+i['NomAp'])
    print("\n")
    exit
