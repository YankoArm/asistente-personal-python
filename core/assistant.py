# core/assistant.py

class Assistant:
    def __init__(self, command_manager):
        self.command_manager = command_manager

    def run(self):
        print("Asistente Yanko v0.1")
        print("Escribe 'ayuda' para ver los comandos o 'salir' para cerrar.\n")

        while True:
            user_input = input("> ").strip()

            if not user_input:
                continue

            if user_input.lower() in ("salir", "exit", "quit"):
                print("Hasta luego 👋")
                break

            self.command_manager.handle(user_input)
