import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

# Asegurarnos de que la carpeta del proyecto está en sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from features import tasks  # usamos tu módulo existente


class TaskApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Asistente Personal - Tareas")
        self.geometry("700x400")

        self._build_ui()
        self._load_tasks()

    def _build_ui(self):
        # --------- Frame superior: formulario de nueva tarea ---------
        top_frame = ttk.Frame(self, padding=10)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        lbl = ttk.Label(top_frame, text="Nueva tarea:")
        lbl.pack(side=tk.LEFT)

        self.entry_task = ttk.Entry(top_frame)
        self.entry_task.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        btn_add = ttk.Button(top_frame, text="Añadir", command=self._on_add_task)
        btn_add.pack(side=tk.LEFT, padx=5)

        # --------- Frame central: listado de tareas ---------
        center_frame = ttk.Frame(self, padding=10)
        center_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        columns = ("id", "text", "status", "created_at", "completed_at")
        self.tree = ttk.Treeview(
            center_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("text", text="Texto")
        self.tree.heading("status", text="Estado")
        self.tree.heading("created_at", text="Creada")
        self.tree.heading("completed_at", text="Completada")

        self.tree.column("id", width=40, anchor=tk.CENTER)
        self.tree.column("text", width=250)
        self.tree.column("status", width=80, anchor=tk.CENTER)
        self.tree.column("created_at", width=130, anchor=tk.CENTER)
        self.tree.column("completed_at", width=130, anchor=tk.CENTER)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(center_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # --------- Frame inferior: botones de acción ---------
        bottom_frame = ttk.Frame(self, padding=10)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        btn_refresh = ttk.Button(bottom_frame, text="Actualizar", command=self._load_tasks)
        btn_refresh.pack(side=tk.LEFT)

        btn_done = ttk.Button(bottom_frame, text="Marcar como hecha", command=self._on_mark_done)
        btn_done.pack(side=tk.LEFT, padx=5)

        btn_pending = ttk.Button(bottom_frame, text="Ver solo pendientes", command=self._show_pending)
        btn_pending.pack(side=tk.LEFT, padx=5)

        btn_all = ttk.Button(bottom_frame, text="Ver todas", command=self._load_tasks)
        btn_all.pack(side=tk.LEFT, padx=5)

    # ----------------- LÓGICA DE NEGOCIO (reutilizando features/tasks) -----------------

    def _load_tasks(self):
        """Carga todas las tareas desde features.tasks y las muestra en el Treeview."""
        self.tree.delete(*self.tree.get_children())
        all_tasks = tasks.list_tasks()

        for t in all_tasks:
            self.tree.insert(
                "",
                tk.END,
                values=(
                    t.get("id"),
                    t.get("text", ""),
                    t.get("status", ""),
                    t.get("created_at", ""),
                    t.get("completed_at", ""),
                )
            )

    def _show_pending(self):
        """Muestra solo tareas pendientes."""
        self.tree.delete(*self.tree.get_children())
        pending = tasks.list_pending()

        for t in pending:
            self.tree.insert(
                "",
                tk.END,
                values=(
                    t.get("id"),
                    t.get("text", ""),
                    t.get("status", ""),
                    t.get("created_at", ""),
                    t.get("completed_at", ""),
                )
            )

    def _on_add_task(self):
        """Callback del botón 'Añadir'."""
        text = self.entry_task.get().strip()
        if not text:
            messagebox.showinfo("Información", "Escribe el texto de la tarea antes de añadir.")
            return

        new_task = tasks.add_task(text)
        if new_task is None:
            messagebox.showwarning("Aviso", "La tarea está vacía, no se ha guardado.")
            return

        self.entry_task.delete(0, tk.END)
        self._load_tasks()

    def _on_mark_done(self):
        """Callback del botón 'Marcar como hecha'."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Información", "Selecciona una tarea de la lista.")
            return

        item_id = selected[0]
        values = self.tree.item(item_id, "values")
        try:
            task_id = int(values[0])
        except (ValueError, TypeError):
            messagebox.showerror("Error", "No se pudo obtener el ID de la tarea seleccionada.")
            return

        updated = tasks.mark_done(task_id)
        if updated is None:
            messagebox.showerror("Error", f"No se encontró la tarea con id {task_id}.")
            return

        self._load_tasks()


def main():
    app = TaskApp()
    app.mainloop()


if __name__ == "__main__":
    main()