import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def clasificar_mensaje(texto):

    prompt = f"""
    Clasifica el siguiente mensaje en una de las siguientes categorías: 'Urgente', 'Moderado' o 'Normal'.

    Mensaje: "{texto}"

    Solo responde con una de las tres palabras: Urgente, Moderado o Normal. No expliques nada.
    """

    response = model.generate_content(prompt)
    resultado = response.text.strip()
    return resultado
