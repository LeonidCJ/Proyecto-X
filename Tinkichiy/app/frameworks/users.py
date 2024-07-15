from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload 

# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    
users_list = [User(id=1, name = "Soledad", surname ="Garcia", age = 67),
         User(id=2, name = "Juan", surname ="Perez", age = 21),
         User(id=3, name = "Ada", surname ="Barrientos", age = 19)]
    
@app.get("/usersjson")
async def usersjson():
    return [{"name":"Soledad","surname":"García Márquez","age":67},
           {"name":"Juan","surname":"Perez","age":21},
           {"name":"Ada","surname":"Barrientos","age":19}]
    
    
@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    
@app.get("/userquery/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}