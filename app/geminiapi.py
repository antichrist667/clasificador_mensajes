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

# --- FORZAR DUPLICACIÓN ---
def clasificador_duplicado_1(texto):
    texto = texto.lower()
    if "urgente" in texto:
        return "Urgente"
    elif "importante" in texto:
        return "Moderado"
    elif "saludo" in texto or "hola" in texto:
        return "Normal"
    else:
        return "Normal"

def clasificador_duplicado_2(texto):
    texto = texto.lower()
    if "urgente" in texto:
        return "Urgente"
    elif "importante" in texto:
        return "Moderado"
    elif "saludo" in texto or "hola" in texto:
        return "Normal"
    else:
        return "Normal"


# --- Bug más realista que 1/0 ---
def bug_index_fuera_de_rango():
    lista = []
    return lista[0]  # esto lanza IndexError


# --- FORZAR VULNERABILIDAD ---
def conectar_a_api():
    api_key = "AIzaSyFAKEKEY-sonar-detecta-esto"  # Esta línea será detectada
    return f"Usando API key: {api_key}"
