
#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
router = APIRouter()

#Levantamos el server Uvicorn
#-uvicorn artistas:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: user

class User(BaseModel):
    id:int
    Nombre: str
    Marca:str
    Color:str
    
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(id=0,Nombre="Altavoz", Marca="JBL", Color="Naranja"),
             User(id=1,Nombre="Home Speaker", Marca="Bose", Color="Gris Espacial"),
             User(id=2,Nombre="Teatro en casa", Marca="Sony", Color="Negro")]


#***Get
@router.get("/artistas/")
async def artistas():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/bocinas/


#***Get con Filtro Path
@router.get("/artistas/{id}", status_code=status.HTTP_302_FOUND)
async def artistas(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha encontrado el usuario") 
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/artistas/1


#***Get con Filtro Query
@router.get("/artistas/", status_code=status.HTTP_302_FOUND)
async def artistas(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha encontrado el usuario") 

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/artistas/?id=1
 
 
#***Post
@router.post("/artistas/", response_model=User, status_code=status.HTTP_201_CREATED)
async def artistas(user:User):
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/artistas/
   
   
    #***Put
@router.put("/artistas/", status_code=status.HTTP_202_ACCEPTED)
async def artistas(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
           raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail="No se ha actualizado")
    else:
        return user
    
    #http://127.0.0.1:8000/artistas/
    
    
        #***Delete
@router.delete("/artistas/{id}", status_code=status.HTTP_200_OK)
async def artistas(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
           raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="No se ha eliminado")
        
    
    #http://127.0.0.1:8000/artistas/1