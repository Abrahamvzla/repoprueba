from fastapi import FastAPI, Request, Response, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
import json

app = FastAPI(
    title="CURSO PRUEBA",
    version="1.0"
)

class Beneficio(BaseModel):
    id: Optional[int] = None
    categoria: str = Field(default="BENEFICIO",min_length=4, max_length=10)
    fecha: str = Field(default="00-00-2024",min_length=10, max_length=10)
    empleados: int = Field(default=1,ge=1)

beneficios = [
    {
        "id": 1,
        "categoria": "BOLSA DE ALIMENTACIÓN",
        "fecha": "14-10-2024",
        "empleados": 20
    },
    {
        "id": 2,
        "categoria": "BOLSA DE PROTEINA",
        "fecha": "15-10-2024",
        "empleados": 20
    }
]


@app.get('/', tags=['home'])
def message():
    return HTMLResponse("<H1>Hola Mundo</H1>")

#@app.post('/personas/{persona_id}')
#async def solicitar(request: Request):
#    data = await request.json()
#    print(data)
#    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type": "application/json"})

@app.get('/beneficios', tags=['beneficios'])
def obtener_lista_beneficios():
    return JSONResponse(content=beneficios)

@app.get('/beneficios/{id}', tags=['beneficios'])
def obtener_un_benefico(id: int):
    for item in beneficios:
        if item["id"] == id:
            #return item
            return JSONResponse(content=item)
    return JSONResponse([])
    #return []

@app.get('/beneficios/', tags=['beneficios'])
def get_benefcios_por_fecha(fecha: str):
    data = [item for item in beneficios if item['fecha'] == fecha]
    return JSONResponse(content=data)
    #return [item for item in beneficios if item['fecha'] == fecha]

@app.post('/beneficios', tags=['beneficios'])
async def crear_beneficio(request: Request):
    data = await request.json()
    beneficios.append(jsonable_encoder(data))
    return beneficios

@app.post('/beneficios', tags=['beneficios'])
def registrar_beneficios(beneficio: Beneficio):
    #beneficios.append(beneficio.dict())
    return beneficios

@app.put('/beneficios/{id}', tags=['beneficios'])
def update_beneficio(id: int, beneficio: Beneficio):
    for item in beneficios:
        if item["id"] == id:
            item['categoria'] = Beneficio.categoria
            item['fecha'] = Beneficio.fecha
            item['empleados'] = Beneficio.empleados
            return beneficios

@app.delete('/beneficios/{id}', tags=['beneficios'])
def delete_beneficios(id: int):
    for item in beneficios:
        if item["id"] == id:
            beneficios.remove(item)
            return beneficios
