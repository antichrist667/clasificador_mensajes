# Clasificador de Mensajes con Zero-Shot Learning

Este proyecto implementa un clasificador de mensajes de texto utilizando Zero-Shot Classification de Hugging Face, integrando LangChain y una interfaz gráfica con Streamlit.

## Características

- Clasificación de mensajes en tres categorías: Urgente, Normal y Moderado
- API REST con FastAPI
- Interfaz gráfica con Streamlit
- Integración con LangChain
- Modelo Zero-Shot de Hugging Face

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd clasificador_mensajesv2
```

2. Crear y activar el entorno virtual:
```bash
# En Windows
python -m venv venv
.\venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### API REST (FastAPI)

1. Iniciar el servidor:
```bash
uvicorn main:app --reload
```

2. La API estará disponible en `http://localhost:8000`
3. Documentación de la API: `http://localhost:8000/docs`

### Interfaz Gráfica (Streamlit)

1. Iniciar la aplicación Streamlit:
```bash
streamlit run app/ui/streamlit_app.py
```

2. La interfaz estará disponible en `http://localhost:8501`

## Estructura del Proyecto

```
clasificador_mensajesv2/
├── app/
│   ├── api/          # Endpoints de la API
│   ├── core/         # Lógica del clasificador
│   └── ui/           # Interfaz de Streamlit
├── tests/            # Pruebas unitarias
├── main.py           # Punto de entrada de la API
└── requirements.txt  # Dependencias del proyecto
```

## Pruebas

Para ejecutar las pruebas:
```bash
pytest
```

## Licencia

Este proyecto está bajo la Licencia MIT. 