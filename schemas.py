from pydantic import *

class ContactoRequestModel(BaseModel):
    nombre:str
    correo:str
    telefono: int
    
class ContactoResponseModel(ContactoRequestModel):
    id:int    