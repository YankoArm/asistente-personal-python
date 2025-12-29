# Asistente Personal en Python

Asistente de línea de comandos y GUI para gestionar **tareas** y **notas**, desarrollado en Python.
Permite al usuario crear, listar, buscar y marcar tareas o notas tanto desde la consola como desde una interfaz gráfica con Tkinter.

Este proyecto forma parte de mi portfolio personal y está orientado al aprendizaje práctico de Python.

---

## 🧠 Descripción general

El asistente permite:

- Crear notas
- Listar notas
- Buscar notas por texto
- Crear tareas pendientes
- Listar todas las tareas
- Listar tareas pendientes
- Marcar tareas como hechas
- Interactuar tanto por consola como por una GUI basada en Tkinter

---

## 🛠 Tecnologías y herramientas

- Python 3.10+  
- Tkinter para la interfaz gráfica  
- Librerías estándar de Python  
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

```md
git clone https://github.com/YankoArm/asistente-personal-python.git
cd asistente-personal-python
python3 -m venv venv
source venv/bin/activate         # macOS / Linux
venv\Scripts\activate            # Windows

```
---

(Actualmente este proyecto no tiene dependencias externas más allá de lo que incluye Python por defecto.)

---

## ▶️ Ejecución

📌 Modo consola

Para usar el asistente desde la terminal:

- python3 main.py
  
🖼 Interfaz gráfica (GUI)

Para abrir la interfaz gráfica:

- python3 main_gui.py

---

## 📌 Uso básico

- Comandos consola

nota <texto> → crear una nota
notas → listar todas las notas
buscar <texto> → buscar notas
tarea <texto> → crear una tarea
tareas → listar todas las tareas
pendientes → listar solo tareas pendientes
hecha <id> → marcar tarea como hecha

Puedes ver la ayuda en consola con:

- help

---

📫 Contacto

- Desarrollado por Yanko Armijo Acevedo
- Correo: yankopro.gramming@gmail.com

---

📝 Licencia

- Este proyecto está abierto para estudio y práctica personal.
- Si decides hacerlo público, puedes agregar una licencia apropiada.
