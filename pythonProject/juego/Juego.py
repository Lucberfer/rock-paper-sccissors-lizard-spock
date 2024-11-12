import tkinter as tk
from juego.gestionJuego import GestionJuego
from juego.interfaz import Interfaz

# Clase principal que inicia el juego y la interfaz
class Juego:
    def __init__(self):
        # Inicializa la lógica del juego y la ventana principal
        self.gestionJuego = GestionJuego()
        self.root = tk.Tk()
        # Configura la interfaz gráfica con la ventana y lógica del juego
        self.interfaz = Interfaz(self.root, self.gestionJuego)

    # Metodo para iniciar el bucle principal de Tkinter
    def ejecutar(self):
        self.root.mainloop()

# Si se ejecuta directamente, crea una instancia de Juego y la lanza
if __name__ == "__main__":
    app = Juego()
    app.ejecutar()
