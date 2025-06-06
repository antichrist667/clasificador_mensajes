from transformers import pipeline
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MessageClassifier:
    def __init__(self, model_name: str = "facebook/bart-large-mnli"):
        """
        Inicializa el clasificador de mensajes usando Zero-Shot Classification.
        
        Args:
            model_name (str): Nombre del modelo de Hugging Face a utilizar
        """
        try:
            self.classifier = pipeline(
                "zero-shot-classification",
                model=model_name,
                device="cpu"  # Cambiar a "cuda" si hay GPU disponible
            )
            self.candidate_labels = ["Urgente", "Normal", "Moderado"]
            logger.info(f"Clasificador inicializado con el modelo {model_name}")
        except Exception as e:
            logger.error(f"Error al inicializar el clasificador: {str(e)}")
            raise

    def classify(self, text: str) -> Dict[str, Any]:
        """
        Clasifica un mensaje de texto en las categorías definidas.
        
        Args:
            text (str): Texto del mensaje a clasificar
            
        Returns:
            Dict[str, Any]: Diccionario con la categoría asignada y detalles de la clasificación
        """
        try:
            # Realizar la clasificación
            result = self.classifier(
                text,
                candidate_labels=self.candidate_labels,
                multi_label=False
            )
            
            # Obtener la categoría con mayor confianza
            max_score_idx = result["scores"].index(max(result["scores"]))
            category = result["labels"][max_score_idx]
            confidence = result["scores"][max_score_idx]
            
            # Preparar el resultado
            classification_result = {
                "category": category,
                "confidence": float(confidence),
                "details": {
                    "all_scores": dict(zip(result["labels"], result["scores"])),
                    "input_text": text
                }
            }
            
            logger.info(f"Mensaje clasificado como '{category}' con confianza {confidence:.2f}")
            return classification_result
            
        except Exception as e:
            logger.error(f"Error al clasificar el mensaje: {str(e)}")
            raise 