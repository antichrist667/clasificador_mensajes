# 🤖 Clasificador Automatizado de Mensajes

Este proyecto permite clasificar mensajes escritos en tres categorías: **Urgente**, **Moderado** o **Normal** utilizando inteligencia artificial (IA) de Gemini (Google) y un servicio web hecho con FastAPI. Además, se cuenta con una interfaz visual creada con Streamlit.

---

## 📌 Objetivos

1. Desarrollar un servicio en Python que reciba mensajes y los clasifique como:
   - 🔴 Urgente
   - 🟡 Moderado
   - 🟢 Normal

2. Usar la API de **Gemini (Google Generative AI)** para realizar la clasificación usando lenguaje natural.

3. Implementar una API REST con **FastAPI** para recibir mensajes y devolver la clasificación.

4. Crear una interfaz visual con **Streamlit** para probar el clasificador fácilmente.

5. Probar el servicio desde **Postman** u otras herramientas similares.

---

## 📁 Estructura del Proyecto

```
clasificador_mensajes/
│
├── app/
│   ├── main.py               # API REST con FastAPI
│   └── geminiapi.py          # Función que usa Gemini para clasificar
│
├── frontend/
│   └── app.py                # Interfaz gráfica con Streamlit
│
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Este archivo
```

---

## 🚀 Cómo Ejecutar el Proyecto

### 1️⃣ Crear y activar el entorno virtual

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

### 2️⃣ Instalar las dependencias

```bash
pip install -r requirements.txt
```

> Asegúrate de tener tu clave de API de Gemini (Google) configurada correctamente.

### 3️⃣ Ejecutar la API con FastAPI

```bash
python -m uvicorn app.main:app --reload
```

- Visita en tu navegador: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para ver la documentación interactiva.

### 4️⃣ Ejecutar la interfaz con Streamlit

```bash
python -m streamlit run frontend/app.py
```

---

## 📦 Endpoints disponibles (FastAPI)

| Método | Endpoint       | Descripción                        |
|--------|----------------|------------------------------------|
| POST   | `/clasificar`  | Recibe un mensaje y lo clasifica  |

Ejemplo de entrada:
```json
{
  "mensaje": "¡Se cayó el servidor principal, ayúdenme!"
}
```

Ejemplo de salida:
```json
{
  "clasificacion": "Urgente"
}
```

---

## 💡 Tecnologías Usadas

- Python 3.x
- FastAPI
- Streamlit
- Google Generative AI (Gemini)
- Uvicorn

---


## 🎥 Video Tutorial

> (Incluye aquí el enlace al video donde expliques cómo corre tu proyecto)

---

## 📩 Contacto

Desarrollado por **Cristian Caiza**  
[Github](https://github.com/antichrist667)