# Asistente Personal en Python

Aplicación de escritorio desarrollada en Python que permite gestionar tareas y notas mediante:

- modo consola  
- interfaz gráfica con Tkinter

Este proyecto forma parte de mi portfolio personal y está enfocado al aprendizaje práctico de Python y diseño modular.

---

## 📌 Estado del proyecto

:construction: Proyecto en desarrollo  
Puede no estar completo en todas las funcionalidades, pero incluye lo esencial para gestionar tareas y notas.

---

## 🧠 Descripción

El asistente permite:

- crear notas rápidas
- listar notas
- buscar notas
- crear tareas pendientes
- listar tareas
- marcar tareas como hechas

El usuario puede interactuar con la aplicación desde consola o mediante la interfaz gráfica (Tkinter).

---

## 🛠 Tecnologías y herramientas

- Python 3 (recomendado >= 3.10)  
- Tkinter (GUI)  
- Módulos estándar de Python  
- JSON para persistencia de datos

---

## 📁 Estructura del proyecto

```text
asistente-personal-python/
│
├── core/                   # Núcleo de lógica del asistente
├── features/               # Funcionalidades (tareas, notas)
├── gui/                    # Interfaz gráfica
├── data/                   # Archivos de datos JSON
│   ├── notes.json
│   └── tasks.json
├── main.py                 # Entrypoint modo consola
├── main_gui.py             # Entrypoint GUI Tkinter
├── .gitignore
└── README.md

```
---

## 🧱 Requisitos

- Python 3.10 o superior
- Entorno virtual (opcional pero recomendado)

---

## 🔧 Instalación

Clona el repositorio:


git clone https://github.com/YankoArm/asistente-personal-python.git
cd asistente-personal-python
python3 -m venv venv
source venv/bin/activate         # macOS / Linux
venv\Scripts\activate            # Windows
pip install -r requirements.txt

---

(Actualmente este proyecto no tiene dependencias externas más allá de lo que incluye Python por defecto.)

---

## ▶️ Ejecución

Modo consola

python3 main.py
Interfaz gráfica (GUI)
python3 main_gui.py

---

## 📌 Notas de uso

- En consola, sigue las instrucciones que se muestran al iniciar.
- En la GUI, usa los botones para añadir y completar tareas.

---

📫 Contacto

- Desarrollado por Yanko Armijo Acevedo
- Correo: yankopro.gramming@gmail.com

---

📝 Licencia

- Este proyecto está abierto para estudio y práctica personal.
- Si decides hacerlo público, puedes agregar una licencia apropiada.
