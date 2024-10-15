from fastapi import FastAPI, Request, Response, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from dto import ApiRequest
import json
app = FastAPI(
    title="Sistema de Beneficios",
    version="1.0"
)
#app.tittle = "Sistema de Beneficios"
#app.version = "0.1"

beneficios = [
    {
        "id":1,
        "categoria": "BOLSA DE ALIMENTACIÓN",
        "fecha": "14-10-2024",
        "empleados":20
    },
     {
        "id":2,
        "categoria": "BOLSA DE PROTEINA",
        "fecha": "15-10-2024",
        "empleados":20
    } 
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse("<H1>Hola Mundo</H1>")
    #return {"Nombre":"Abraham"}
    #return {"code": "hola  acabas de nacer"}

@app.post('/personas/{persona_id}')
async def solicitar(request: Request):
    data=await request.json()
    print(data)
    return Response(status_code=200, content=json.dumps(data), headers={"Content-Type":"application/json"})

@app.get('/beneficios', tags=['beneficios'])
def get_benefcios():
    return beneficios


@app.get('/beneficios/{id}', tags=['beneficios'])
def get_beneficos(id: int):
    for item in beneficios:
        if item["id"] == id:
            return item
    return []


#@app.get('/beneficios/', tags=['beneficios'])
#def get_benefcios_por_fecha(fecha: str):
#    return fecha

@app.get('/beneficios/', tags=['beneficios'])
def get_benefcios_por_fecha(fecha: str):
    return [item for item in beneficios if item['fecha'] == fecha]
#######
@app.post('/beneficios', tags=['beneficios'])
async def crear_beneficio(request: ApiRequest):
    data = request
    beneficios.append(jsonable_encoder(data))
    return beneficios

@app.put('/beneficios/{id}',tags=['beneficios'])
def update_beneficio(id: int, categoria: str= Body(), fecha: str=Body(), empleados: int=Body()):
    for item in beneficios:
        if item["id"]==id:
            item['categoria']=categoria,
            item['fecha']=fecha,
            item['empleados']=empleados
            return beneficios
        
