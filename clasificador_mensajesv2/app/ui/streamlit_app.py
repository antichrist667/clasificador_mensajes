import streamlit as st
import requests
import json
from typing import Dict, Any
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Clasificador de Mensajes",
    page_icon="📝",
    layout="wide"
)

# Título y descripción
st.title("📝 Clasificador de Mensajes")
st.markdown("""
Esta aplicación utiliza Zero-Shot Classification para categorizar mensajes de texto en tres niveles:
- 🔴 **Urgente**: Mensajes que requieren atención inmediata
- 🟡 **Moderado**: Mensajes que requieren atención pero no son críticos
- 🟢 **Normal**: Mensajes que pueden ser atendidos en el tiempo normal
""")

# Inicializar el historial de clasificaciones en la sesión
if "classification_history" not in st.session_state:
    st.session_state.classification_history = []

def classify_message(text: str) -> Dict[str, Any]:
    """
    Envía el mensaje a la API para su clasificación.
    
    Args:
        text (str): Texto del mensaje a clasificar
        
    Returns:
        Dict[str, Any]: Resultado de la clasificación
    """
    try:
        response = requests.post(
            "http://localhost:8000/classify",
            json={"text": text}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error al comunicarse con la API: {str(e)}")
        return None

def display_classification_result(result: Dict[str, Any]):
    """
    Muestra el resultado de la clasificación de forma visual.
    
    Args:
        result (Dict[str, Any]): Resultado de la clasificación
    """
    if not result:
        return
    
    # Crear columnas para mostrar el resultado
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Resultado de la Clasificación")
        
        # Mostrar la categoría con un indicador de color
        category_colors = {
            "Urgente": "🔴",
            "Moderado": "🟡",
            "Normal": "🟢"
        }
        
        st.markdown(f"""
        ### {category_colors[result['category']]} Categoría: {result['category']}
        **Confianza**: {result['confidence']:.2%}
        """)
        
        # Mostrar los scores de todas las categorías
        st.subheader("Scores por Categoría")
        scores_df = pd.DataFrame(
            list(result['details']['all_scores'].items()),
            columns=['Categoría', 'Confianza']
        )
        fig = px.bar(
            scores_df,
            x='Categoría',
            y='Confianza',
            color='Categoría',
            color_discrete_map={
                'Urgente': 'red',
                'Moderado': 'orange',
                'Normal': 'green'
            }
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Detalles del Mensaje")
        st.text_area(
            "Mensaje Original",
            result['details']['input_text'],
            height=150,
            disabled=True
        )

# Interfaz principal
st.subheader("Ingrese un mensaje para clasificar")
message = st.text_area(
    "Mensaje",
    placeholder="Escriba su mensaje aquí...",
    height=100
)

if st.button("Clasificar Mensaje", type="primary"):
    if message:
        with st.spinner("Clasificando mensaje..."):
            result = classify_message(message)
            if result:
                # Agregar al historial
                st.session_state.classification_history.append(result)
                # Mostrar el resultado
                display_classification_result(result)
    else:
        st.warning("Por favor, ingrese un mensaje para clasificar.")

# Mostrar historial de clasificaciones
if st.session_state.classification_history:
    st.subheader("Historial de Clasificaciones")
    history_df = pd.DataFrame([
        {
            "Mensaje": item["details"]["input_text"],
            "Categoría": item["category"],
            "Confianza": f"{item['confidence']:.2%}"
        }
        for item in st.session_state.classification_history
    ])
    st.dataframe(history_df, use_container_width=True)
    
    # Botón para limpiar el historial
    if st.button("Limpiar Historial"):
        st.session_state.classification_history = []
        st.experimental_rerun() 