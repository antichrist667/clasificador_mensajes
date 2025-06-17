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

# --- Duplicación real forzada (más de 10 líneas) ---
def clasificacion_demo1(texto):
    if "urgente" in texto.lower():
        return "Urgente"
    elif "importante" in texto.lower():
        return "Moderado"
    elif "hola" in texto.lower():
        return "Normal"
    else:
        return "Normal"

def clasificacion_demo2(texto):
    if "urgente" in texto.lower():
        return "Urgente"
    elif "importante" in texto.lower():
        return "Moderado"
    elif "hola" in texto.lower():
        return "Normal"
    else:
        return "Normal"

# --- Bug más realista que 1/0 ---
def bug_index_fuera_de_rango():
    lista = []
    return lista[0]  # esto lanza IndexError


def sin_test_sonar():
    return "Esta función no está testeada"

api_key_expuesta = "AIzaSyFAKEKEY-sonar-detecta-esto"