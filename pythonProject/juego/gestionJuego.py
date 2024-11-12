from random import choice

class GestionJuego:
    def __init__(self):
        # piedra rompe tijeras
        # piedra aplasta lagarto
        # papel envuelve piedra
        # papel desautoriza Spock
        # tijeras corta papel
        # tijera decapita lagarto
        # lagarto envenena Spock
        # lagarto come papel
        # Spock rompe tijeras
        # Spock vaporiza piedra

        # Inicializa las opciones del juego y las reglas de qué vence a qué
        self.opciones = ["piedra", "papel", "tijeras", "lagarto", "spock"]
        self.reglas = {
            "piedra": ["tijeras", "lagarto"],
            "papel": ["piedra", "spock"],
            "tijeras": ["papel", "lagarto"],
            "lagarto": ["spock", "papel"],
            "spock": ["tijeras", "piedra"]
        }

    # Selecciona una opción aleatoria para la máquina
    def obtener_opcion_maquina(self):
        return choice(self.opciones)

    # Determina el ganador comparando las elecciones del jugador y de la máquina
    def determinar_ganador(self, jugador, maquina):
        if jugador == maquina:
            return "empate"
        elif maquina in self.reglas[jugador]:
            return "jugador"
        else:
            return "maquina"