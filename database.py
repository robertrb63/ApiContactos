from peewee import*

dbLite = SqliteDatabase('agenda.db')

class Contacto(Model):
    nombre=TextField()
    correo=TextField()
    telefono=IntegerField()
   
    class Meta:
        database = dbLite
        table_name = 'Contactos'

dbLite.connect()

def cargar_contactos():
    contactos = []
    for cont in Contacto.select().dicts():
        contactos.append(cont)
    return contactos    