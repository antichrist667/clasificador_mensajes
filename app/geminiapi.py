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

def simular_bug():
    return 1 / 0

def mensaje_demo():
    texto = "Duplicación SonarCloud"
    print(texto)
    return texto

def mensaje_demo2():
    texto = "Duplicación SonarCloud"
    print(texto)
    return texto

def sin_test_sonar():
    return "Esta función no está testeada"

api_key_expuesta = "AIzaSyFAKEKEY-sonar-detecta-esto"