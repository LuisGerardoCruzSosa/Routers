#########################################Primera Parte################################################
# Instalación del framwork fastApi, código:
# -pip install fastapi-

#Instalación del Servidor Uvicorn, código:
#-pip install "uvicorn[standard]"-

# Instalación del framwork fastApi, código:
# -pip install fastapi[all]-

#-uvicorn main:app --reload-
#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 

from Routers import televisiones, bocinas, carros, ciudades, computadoras, mochilas, escuelas, artistas, celulares, relojes
#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

app.include_router(televisiones.router)
app.include_router(bocinas.router)
app.include_router(carros.router)
app.include_router(ciudades.router)
app.include_router(computadoras.router)
app.include_router(mochilas.router)
app.include_router(escuelas.router)
app.include_router(artistas.router)
app.include_router(celulares.router)
app.include_router(relojes.router)


@app.get("/")
async def imprimir():
    return "Hola estudiantes"

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/