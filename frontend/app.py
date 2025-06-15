import requests
import streamlit as st

st.set_page_config(page_title="Clasificador de Mensajes", layout="centered")
st.title("Clasificación de Mensajes con Gemini")

mensaje = st.text_area("✉️ Escribe un mensaje para clasificar:", height=150)

if st.button("Clasificar"):
    if mensaje.strip():
        try:
            response = requests.post("http://localhost:8000/clasificar", json={"texto": mensaje})
            if response.status_code == 200:
                categoria = response.json()["clasificación"]
                st.success(f"Clasificación: {categoria}")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"No se pudo conectar con la API: {e}")
    else:
        st.warning("Escribe un mensaje antes de clasificar.")
