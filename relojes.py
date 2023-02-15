
#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import APIRouter, HTTPException, status
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
router = APIRouter()

#Levantamos el server Uvicorn
#-uvicorn relojes:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: user

class User(BaseModel):
    id:int
    Nombre: str
    Marca:str
    Color:str
    
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(id=0,Nombre="DATEJUST", Marca="Rolex", Color="Plateado"),
             User(id=1,Nombre="Analogico", Marca="Casio", Color="Negro"),
             User(id=2,Nombre="Pro Diver", Marca="Invicta", Color="Dorado")]


#***Get
@router.get("/relojes/")
async def relojes():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/relojes/


#***Get con Filtro Path
@router.get("/relojes/{id}", status_code=status.HTTP_302_FOUND)
async def relojes(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha encontrado el usuario") 
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/relojes/1


#***Get con Filtro Query
@router.get("/relojes/", status_code=status.HTTP_302_FOUND)
async def relojes(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
       raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se ha encontrado el usuario") 

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/relojes/?id=1
 
 
#***Post
@router.post("/relojes/", response_model=User, status_code=status.HTTP_201_CREATED)
async def relojes(user:User):
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el usuario ya existe")
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/relojes/
   
   
    #***Put
@router.put("/relojes/", status_code=status.HTTP_202_ACCEPTED)
async def relojes(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
           raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail="No se ha actualizado")
    else:
        return user
    
    #http://127.0.0.1:8000/relojes/
    
    
        #***Delete
@router.delete("/relojes/{id}", status_code=status.HTTP_200_OK)
async def relojes(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           return "El registro se ha eliminado"
       
    if not found:
           raise HTTPException(status_code= status.HTTP_304_NOT_MODIFIED,detail="No se ha eliminado")
        
    
    #http://127.0.0.1:8000/relojes/1