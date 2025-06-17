from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.geminiapi import ( 
    clasificar_mensaje,
    conectar_a_api,
    bug_index_fuera_de_rango
)
app = FastAPI()

class Mensaje(BaseModel):
    texto: str

# smell
if True:
    print("Esto no debería estar aquí")    

@app.post("/clasificar")
def clasificar(mensaje: Mensaje):
    try:
        resultado = clasificar_mensaje(mensaje.texto)
        return {"clasificación": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# endpoint
@app.get("/demo-sonar")
def demo_sonar():
    from app.geminiapi import simular_bug, api_key_expuesta

    try:
        simular_bug()  
    except IndexError: 
        pass

    clave = api_key_expuesta  
    return {"status": "demo ejecutado"}