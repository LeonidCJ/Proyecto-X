from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload 

# Entidad user

class User(BaseModel):
    
    id: int
    name: str
    surname:str
    age: int
    
# base de datos inventada
    
users_list = [User(id=1, name = "Soledad", surname ="Garcia", age = 67),
         User(id=2, name = "Juan", surname ="Perez", age = 21),
         User(id=3, name = "Ada", surname ="Barrientos", age = 19)]

# Json manual
  
@app.get("/usersjson")
async def usersjson():
    return [{"name":"Soledad","surname":"García Márquez","age":67},
           {"name":"Juan","surname":"Perez","age":21},
           {"name":"Ada","surname":"Barrientos","age":19}]
    
    
@app.get("/users")
async def users():
    return users_list

#path

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#query    
    
@app.get("/user/")
async def user(id: int):
    return search_user(id)
    
#post

@app.post("/user/", status_code = 201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    
    users_list.append(user)
    return user 
        
#put

@app.put("/user/")
async def user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_list): 
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"error": "No se ha encontrado el usuario"}
    
    return user
    
#delete

@app.delete("/user/{id}")
async def user(id: int):
    
    found = False
    
    for index, saved_user in enumerate(users_list): 
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return {"error": "No se ha eliminado el usuario"}

def search_user( id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}