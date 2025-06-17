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
# 🔍 Smell de demostración
if True:
    print("Esto no debería estar aquí (smell)")    

@app.post("/clasificar")
def clasificar(mensaje: Mensaje):
    try:
        resultado = clasificar_mensaje(mensaje.texto)
        return {"clasificación": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# ✅ NUEVO endpoint para forzar detecciones en SonarCloud
@app.get("/demo-sonar")
def demo_sonar():
    from app.geminiapi import simular_bug, api_key_expuesta

    try:
        simular_bug()  # Forzar error
    except IndexError:  # Actualiza la excepción
        pass

    clave = api_key_expuesta  # Usar clave vulnerable

    return {"status": "demo ejecutado"}
