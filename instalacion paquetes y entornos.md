## PREPARATIVOS PARA SISTEMA FASTAPI

### TENER INSTALADO PYTHON


Posterior a instalar python y aperturar la carpeta donde se va a trabajar, , instalamos el paquete de entorno virtual.

el comando para instalar modulo es:
``python -m  modulo a instalar`` 

para instalar entorno virtual

``python -m venv venv`` 

Activar entorno virtual:
En windows:
``nombre_de_entorno/Scripts/activate``
En Linux:
``nombre_de_entorno/bin/activate``

en caso de error

``Set-ExecutionPolicy RemoteSigned``

### Instalar modulos a usar

`` pip install fastapi``

Para instalar desde archivo txt

``pip install -r requirements.txt``

Si se requiere actualizar version de pip

`` python -m pip install --upgrade pip``

## Ejecutar aplicacion

``uvicorn nombrearchivo:nombreaplicacion``

ejemplo

``uvicorn main:app``

para aplicar ejecutar aplicacion y que detecte cambios realizados para recargar el servicio.

``uvicorn main:app --reload``

Asignar puerto

``uvicorn main:app --8080``