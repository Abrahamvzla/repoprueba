# manejo de solicitudes y validaciones

from pydantic import BaseModel,Field


se crea una clase heredando clase Base Model
dentro de la clase se iguala los atributos a field ( y se cloca las validaciones)

```
class beneficio(BaseModel):
    id: Optional[int] = None
    categoria: str = Field(default="Beneficio",min_length=4, max_length=10)
    fecha: str = Field(default="00-00-2024", min_length=10,max_length=10)
    empleados: int = Field(default=1, min_length=1)
```

de requerir usar valores default , se usa otra clase con squeme , donde estarian los default
```
class beneficio(BaseModel):
    id: Optional[int] = None
    categoria: str = Field(min_length=4, max_length=10)
    fecha: str = Field(min_length=10,max_length=10)
    empleados: int = Field(min_length=1)

    class Config:
        scheme_extra={
            "example": {
                "id" : 1,
                "categoria":"BOLSA",
                "fecha":"00-00-2024",
                "empleados":2
            }
        }
```