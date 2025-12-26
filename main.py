# -*- coding: utf-8 -*-

import os
import sys

# Asegurarnos de que la carpeta del proyecto está en sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from features import notes
from features import tasks
from core.assistant import Assistant
from core.commands import CommandManager


def cmd_nota(args):
    if not args:
        print("Tienes que escribir el texto de la nota.")
        return

    note = notes.add_note(args)
    if note is None:
        print("La nota esta vacia, no se guarda.")
        return

    print(f"Nota {note['id']} guardada.")

def cmd_notas(args):
    all_notes = notes.list_notes()
    if not all_notes:
        print("No hay notas todavia.")
        return

    for n in all_notes:
        print(f"[{n['id']}] {n['created_at']} - {n['text']}")

def cmd_buscar(args):
    if not args:
        print("Debes escribir un texto para buscar.")
        return

    results = notes.search_notes(args)

    if not results:
        print("No se encontraron notas que coincidan.")
        return

    for n in results:
        print(f"[{n['id']}] {n['created_at']} - {n['text']}")

def cmd_tarea(args):
    if not args:
        print("Tienes que escribir el texto de la tarea.")
        return

    task = tasks.add_task(args)
    if task is None:
        print("La tarea esta vacia, no se guarda.")
        return

    print(f"Tarea {task['id']} creada como pendiente.")

def cmd_tareas(args):
    all_tasks = tasks.list_tasks()
    if not all_tasks:
        print("No hay tareas todavia.")
        return

    for t in all_tasks:
        status = t.get("status", "pendiente")
        print(f"[{t['id']}] ({status}) {t['text']} - creada: {t['created_at']}")

def cmd_pendientes(args):
    pending = tasks.list_pending()
    if not pending:
        print("No hay tareas pendientes.")
        return

    for t in pending:
        print(f"[{t['id']}] {t['text']} - creada: {t['created_at']}")

def cmd_hecha(args):
    args = args.strip()
    if not args:
        print("Debes indicar el id de la tarea. Ejemplo: hecha 3")
        return

    if not args.isdigit():
        print("El id de la tarea debe ser un numero.")
        return

    task_id = int(args)
    updated = tasks.mark_done(task_id)

    if updated is None:
        print(f"No se encontro la tarea con id {task_id}.")
    else:
        print(f"Tarea {task_id} marcada como hecha.")


def main():
    cmd_manager = CommandManager()

    # Registrar comandos
    cmd_manager.register("nota", cmd_nota, "Guardar una nota rapida")
    cmd_manager.register("tarea", cmd_tarea, "Anadir una tarea pendiente")
    cmd_manager.register("tareas", cmd_tareas, "Listar todas las tareas")
    cmd_manager.register("pendientes", cmd_pendientes, "Listar solo tareas pendientes")
    cmd_manager.register("hecha", cmd_hecha, "Marcar una tarea como hecha por id")
    cmd_manager.register("notas", cmd_notas, "Listar todas las notas")
    cmd_manager.register("buscar", cmd_buscar, "Buscar notas que contengan un texto")


    asistente = Assistant(cmd_manager)
    asistente.run()


if __name__ == "__main__":
    main()
