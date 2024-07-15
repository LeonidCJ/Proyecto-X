from fastapi import FastAPI

app = FastAPI()

# Inicia el server: uvicorn main:app --reload 

@app.get("/")
async def root():
    return "Hola FastAPI"