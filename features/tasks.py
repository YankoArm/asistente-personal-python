# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime

# Carpeta base del proyecto (donde esta main.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")


def _load_tasks():
    """Carga las tareas desde el fichero JSON. Devuelve una lista."""
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Si el fichero esta corrupto, empezamos de cero
            return []


def _save_tasks(tasks):
    """Guarda la lista de tareas en el fichero JSON."""
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(text):
    """Crea una nueva tarea pendiente y la guarda. Devuelve la tarea creada."""
    text = text.strip()
    if not text:
        return None

    tasks = _load_tasks()
    new_id = tasks[-1]["id"] + 1 if tasks else 1

    task = {
        "id": new_id,
        "text": text,
        "status": "pendiente",  # 'pendiente' o 'hecha'
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "completed_at": None,
    }

    tasks.append(task)
    _save_tasks(tasks)
    return task


def list_tasks():
    """Devuelve la lista de todas las tareas."""
    return _load_tasks()


def list_pending():
    """Devuelve solo tareas pendientes."""
    tasks = _load_tasks()
    return [t for t in tasks if t.get("status") == "pendiente"]


def mark_done(task_id):
    """
    Marca una tarea como hecha por id.
    Devuelve la tarea modificada o None si no se encuentra.
    """
    tasks = _load_tasks()
    found = None

    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "hecha"
            t["completed_at"] = datetime.now().isoformat(timespec="seconds")
            found = t
            break

    if found is None:
        return None

    _save_tasks(tasks)
    return found
