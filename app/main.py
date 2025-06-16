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
        
        prompt = f"""
        Clasifica el siguiente mensaje en una de las siguientes categorías: 'Urgente', 'Moderado' o 'Normal'.

        Mensaje: "{mensaje.texto}"

        Solo responde con una de las tres palabras: Urgente, Moderado o Normal. No expliques nada.
        """
        
        resultado = clasificar_mensaje(mensaje.texto)
        return {"clasificación": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
