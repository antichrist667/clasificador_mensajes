from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
import uvicorn

from app.core.classifier import MessageClassifier

app = FastAPI(
    title="Clasificador de Mensajes API",
    description="API para clasificar mensajes de texto usando Zero-Shot Classification",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar el clasificador
classifier = MessageClassifier()

class Message(BaseModel):
    text: str

class ClassificationResponse(BaseModel):
    category: str
    confidence: float
    details: Dict[str, Any]

@app.post("/classify", response_model=ClassificationResponse)
async def classify_message(message: Message):
    """
    Clasifica un mensaje de texto en las categorías: Urgente, Normal o Moderado.
    
    Args:
        message (Message): Objeto que contiene el texto a clasificar
        
    Returns:
        ClassificationResponse: Objeto con la categoría asignada y detalles de la clasificación
    """
    try:
        result = classifier.classify(message.text)
        return ClassificationResponse(
            category=result["category"],
            confidence=result["confidence"],
            details=result["details"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """
    Endpoint para verificar el estado de la API.
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 