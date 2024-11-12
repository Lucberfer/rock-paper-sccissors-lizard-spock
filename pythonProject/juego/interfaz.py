import tkinter as tk
from PIL import Image, ImageTk

class Interfaz:
    def __init__(self, root, gestionJuego):
        # Configuración inicial de la interfaz
        self.gestionJuego = gestionJuego
        self.root = root
        self.root.title("Piedra, papel, tijeras, lagarto, Spock")
        self.root.geometry("1000x400")

        dark_gray = "#2e2e2e"
        self.root.configure(bg=dark_gray)

        # Carga y ajuste de imágenes para las opciones del juego
        self.imagenes = {
            "piedra": ImageTk.PhotoImage(Image.open("piedra.png").resize((80, 80))),
            "papel": ImageTk.PhotoImage(Image.open("papel.png").resize((80, 80))),
            "tijeras": ImageTk.PhotoImage(Image.open("tijeras.png").resize((80, 80))),
            "lagarto": ImageTk.PhotoImage(Image.open("lagarto.png").resize((80, 80))),
            "spock": ImageTk.PhotoImage(Image.open("spock.png").resize((80, 80)))
        }

        # Etiquetas para mostrar las elecciones del jugador y la máquina
        self.textoJugador = tk.Label(self.root, text="Elección del jugador: ", font=("Arial", 12))
        self.textoJugador.pack(side="left", padx=20, pady=20)

        self.textoMaquina = tk.Label(self.root, text="Elección de la máquina: ", font=("Arial", 12))
        self.textoMaquina.pack(side="right", padx=20, pady=20)

        # Etiqueta para mostrar el resultado
        self.textoResultado = tk.Label(self.root, text="El resultado aparecerá aquí", font=("Arial", 14, "bold"))
        self.textoResultado.pack(pady=20)

        # Crear botones con imágenes para cada opción de juego del jugador
        self.frameBotones = tk.Frame(self.root, bg=dark_gray)
        self.frameBotones.pack(pady=20)

        # Crear un botón con imagen para cada opción, que al hacer clic llama a jugar
        for opcion in self.gestionJuego.opciones:
            boton = tk.Button(self.frameBotones, image=self.imagenes[opcion], command=lambda opcion = opcion: self.jugar(opcion))
            boton.pack(side="left", padx=5)

    def jugar(self, eleccionJugador):
        # Obtener elección aleatoria de la máquina y determinar el resultado
        eleccionMaquina = self.gestionJuego.obtener_opcion_maquina()
        resultado = self.gestionJuego.determinar_ganador(eleccionJugador, eleccionMaquina)

        # Actualizar etiquetas para mostrar las elecciones del jugador y de la máquina
        self.textoJugador.config(text=f"Elección del jugador: {eleccionJugador.capitalize()}")
        self.textoMaquina.config(text=f"Elección de la máquina: {eleccionMaquina.capitalize()}")

        # Mostrar el resultado en la etiqueta textoResultado con color de texto correspondiente
        if resultado == "empate":
            self.textoResultado.config(text="Empataste ._.", fg="blue")
        elif resultado == "jugador":
            self.textoResultado.config(text="Ganaste campeón, toma una galleta", fg="green")
        else:
            self.textoResultado.config(text="Perdiste la galleta", fg="red")
