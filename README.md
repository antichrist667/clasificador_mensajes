# 🤖 Clasificador Automatizado de Mensajes

Este proyecto permite clasificar mensajes escritos en tres categorías: **Urgente**, **Moderado** o **Normal** utilizando inteligencia artificial (IA) de Gemini (Google) y un servicio web hecho con FastAPI. Además, se cuenta con una interfaz visual creada con Streamlit.

---

## 📌 Objetivossss

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

## 📦 Endpoints disponibles 

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
---

## 🧪 Tests y Análisis de Calidad con SonarCloud

Este proyecto está integrado con **SonarCloud**, una plataforma que analiza la calidad del código, detecta errores, vulnerabilidades, duplicaciones y mide la cobertura de pruebas.

### 📌 ¿Qué analiza SonarCloud?

| Categoría           | Qué detecta                                                               |
|---------------------|----------------------------------------------------------------------------|
| 🐞 Bugs              | Errores de lógica como divisiones por cero o código que puede fallar      |
| 🧼 Code Smells       | Malas prácticas como `if True:`, `print()` innecesarios o código confuso   |
| 🔐 Vulnerabilidades  | Claves de API hardcodeadas o fragmentos que exponen seguridad              |
| ♻️ Duplicaciones     | Bloques de código repetido en diferentes partes del proyecto               |
| 🧪 Cobertura de Tests| Cuánto del código está cubierto por pruebas (`pytest + coverage`)         |
| 🚦 Quality Gate      | Condiciones mínimas de calidad que el proyecto debe cumplir                |

### ✅ ¿Cómo se ejecutan los tests?

## 🛠 Integración de SonarCloud con GitHub Actions

Este proyecto está completamente integrado con **SonarCloud** a través de **GitHub Actions**, lo que permite ejecutar automáticamente el análisis de calidad de código en cada push o pull request.

### 🔁 ¿Cómo funciona el flujo?

El flujo de análisis con GitHub Actions y SonarCloud funciona de la siguiente manera:

1. **Push o Pull Request a la rama `main`**
   - Cada vez que subes cambios (`git push`) o haces un Pull Request hacia la rama principal, se activa el flujo automático.

2. **GitHub ejecuta el workflow `sonar.yml`**
   - Este workflow se encuentra en `.github/workflows/sonar.yml`
   - Dentro del flujo se hacen los siguientes pasos:
     - Se instala Python
     - Se instalan las dependencias
     - Se ejecutan los tests con cobertura
     - Se genera un archivo `coverage.xml`
     - Se lanza el escaneo de SonarCloud usando la API Key

3. **Autenticación con SonarCloud**
   - Se utiliza una clave secreta llamada `SONAR_TOKEN`, guardada como secret en GitHub:
     - `Settings > Secrets > Actions > New repository secret`
     - Name: `SONAR_TOKEN`
     - Value: (token generado desde SonarCloud)

4. **Envío del análisis a SonarCloud**
   - GitHub Actions envía:
     - El código fuente
     - El archivo `coverage.xml`
     - Información del commit
   - SonarCloud procesa el análisis y lo muestra en su plataforma online.

5. **Visualización de resultados**
   - Puedes ver el estado del análisis en:
     - `https://sonarcloud.io/project/overview?id=antichrist667_clasificador_mensajes`
   - Aquí verás:
     - Bugs, code smells, duplicaciones, vulnerabilidades, cobertura, y el estado del Quality Gate

### 📦 Resultado
Cada cambio en el código es analizado automáticamente.

Las métricas de calidad, seguridad y cobertura están siempre actualizadas.

Puedes detectar errores antes de que lleguen a producción.
---

## 📚 Casos de Uso del Análisis con SonarCloud

A continuación se presentan ejemplos prácticos de cómo SonarCloud detecta distintos tipos de problemas en el código fuente. Estos casos fueron implementados directamente en este proyecto para fines educativos y demostrativos.

### 🐞 1. Detección de Bugs

**Caso implementado:**  
En el archivo `geminiapi.py`, se define una función `simular_bug()` que contiene una división por cero:

```python
def simular_bug():
    return 1 / 0
```

**Resultado:**  
SonarCloud detecta esta línea como un **bug crítico**, ya que puede lanzar una excepción en tiempo de ejecución.

---

### 🧼 2. Detección de Code Smells

**Caso implementado:**  
En `main.py`, se colocó una condición redundante y un `print()` innecesario:

```python
if True:
    print("Esto no debería estar aquí")
```

**Resultado:**  
SonarCloud lo marca como un **code smell**, sugiriendo eliminar la lógica innecesaria para mejorar la mantenibilidad.

---

### 🔐 3. Detección de Vulnerabilidades

**Caso implementado:**  
En `geminiapi.py`, se colocó intencionalmente una clave falsa:

```python
api_key_expuesta = "AIzaSyFAKEKEY-sonar-detecta-esto"
```

**Resultado:**  
SonarCloud lo identifica como una **vulnerabilidad de seguridad** en la categoría *Security Hotspots*, advirtiendo que no se deben dejar claves visibles en el código.

---

### ♻️ 4. Detección de Código Duplicado

**Caso implementado:**  
Se duplicó el siguiente bloque en dos funciones distintas:

```python
def mensaje_demo():
    texto = "Duplicación SonarCloud"
    print(texto)
    return texto

def mensaje_demo2():
    texto = "Duplicación SonarCloud"
    print(texto)
    return texto
```

**Resultado:**  
SonarCloud detecta la **duplicación** y sugiere refactorizar el código.

---

### 🧪 5. Análisis de Cobertura de Pruebas

**Caso implementado:**  
Se creó una función `sin_test_sonar()` en `geminiapi.py` que no está cubierta por tests al inicio.

```python
def sin_test_sonar():
    return "Esta función no está testeada"
```

**Resultado:**  
SonarCloud reduce el porcentaje de **cobertura** total y muestra qué líneas no han sido cubiertas por pruebas.

---

### 🚦 6. Quality Gate (Evaluación Final de Calidad)

**Caso implementado:**  
Con la combinación de bugs, smells, clave visible y baja cobertura, el Quality Gate falló automáticamente.

**Resultado:**  
El estado del proyecto en SonarCloud pasa de **Passed (🟢)** a **Failed (🔴)**, exigiendo correcciones antes de aprobar la calidad del código.

---


## 🎥 Video Tutorial

> (Incluye aquí el enlace al video donde expliques cómo corre tu proyecto)

---

## 📩 Contacto

Desarrollado por **Cristian Caiza**  
[Github](https://github.com/antichrist667)