from pydantic import BaseModel
class ApiRequest(BaseModel):
    id:int
    categoria:str
    fecha:str
    empleados:int
    