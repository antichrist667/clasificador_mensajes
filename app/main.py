from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.geminiapi import ( 
    clasificar_mensaje,
    mensaje_demo,# activamos el uso de la clave vulnerable
    mensaje_demo2,
    simular_bug,
    sin_test_sonar,
    api_key_expuesta  # activamos el uso de la clave vulnerable
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
    from app.geminiapi import simular_bug, mensaje_demo, mensaje_demo2, api_key_expuesta

    try:
        simular_bug()  # Forzar error
    except ZeroDivisionError:
        pass

    mensaje_demo()
    mensaje_demo2()
    clave = api_key_expuesta  # Usar clave vulnerable

    return {"status": "demo ejecutado"}