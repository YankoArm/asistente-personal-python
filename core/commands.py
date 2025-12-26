# core/commands.py

class CommandManager:
    def __init__(self):
        self.commands = {}

    def register(self, name, handler, help_text=""):
        self.commands[name] = {
            "handler": handler,
            "help": help_text
        }

    def handle(self, user_input):
        parts = user_input.split(" ", 1)
        name = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if name == "ayuda":
            self.show_help()
            return

        cmd = self.commands.get(name)
        if not cmd:
            print(f"Comando desconocido: {name}. Escribe 'ayuda' para ver opciones.")
            return

        cmd["handler"](args)

    def show_help(self):
        print("Comandos disponibles:")
        for name, info in self.commands.items():
            texto = info["help"] or "(sin descripción)"
            print(f"  {name:<10} - {texto}")
        print("  salir      - Cerrar el asistente")
