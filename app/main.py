from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.geminiapi import clasificar_mensaje

app = FastAPI()

class Mensaje(BaseModel):
    texto: str

if True:
    print("Esto no debería estar aquí (smell)")    

@app.post("/clasificar")
def clasificar(mensaje: Mensaje):
    try:
        resultado = clasificar_mensaje(mensaje.texto)
        return {"clasificación": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
