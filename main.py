from fastapi import FastAPI
from httpcore import HTTPConnection
from database import dbLite as connection
from database import *
from schemas import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='api contactos', descripcion='api 1ra versión')
#correccion CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 #conectar y desconectar api
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect() 
    connection.create_tables([Contacto])   
  
@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():        
        connection.close()

@app.post('/api/v1/agregar', tags=["Contacto"])
async def agregar_contacto(contacto_request:ContactoRequestModel):
    cont=Contacto.create(
        nombre = contacto_request.nombre,
        correo = contacto_request.correo,
        telefono = contacto_request.telefono
    )
    
@app.delete('/api/v1/eliminar/{contacto_id}', tags=["Contacto"])
async def eliminar_contacto(contacto_id):
    cont=Contacto.select().where(Contacto.id == contacto_id).first()
    
    if cont:
        cont.delete_instance()
        return True, 'contacto eliminado exitosamente'
    else:
        return HTTPConnection(404, 'el contacto no se elimidado')

@app.get('/api/v1/contactos', tags=["Contacto"])
def lista_contactos():
    tmp = cargar_contactos()
    return tmp