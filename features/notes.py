# -*- coding: utf-8 -*-

import json
import os
from datetime import datetime

# Carpeta base del proyecto (donde esta main.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")


def _load_notes():
    """Carga las notas desde el fichero JSON. Devuelve una lista."""
    if not os.path.exists(NOTES_FILE):
        return []

    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Si el fichero esta corrupto, empezamos de cero
            return []


def _save_notes(notes):
    """Guarda la lista de notas en el fichero JSON."""
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)


def add_note(text):
    """Crea una nueva nota y la guarda. Devuelve la nota creada."""
    text = text.strip()
    if not text:
        return None

    notes = _load_notes()
    new_id = notes[-1]["id"] + 1 if notes else 1

    note = {
        "id": new_id,
        "text": text,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }

    notes.append(note)
    _save_notes(notes)
    return note


def list_notes():
    """Devuelve la lista de todas las notas."""
    return _load_notes()

def search_notes(query):
    """Devuelve las notas que contienen el texto de 'query'."""
    query = query.strip().lower()
    if not query:
        return []

    notes = _load_notes()
    result = []

    for n in notes:
        if query in n["text"].lower():
            result.append(n)

    return result
