class Jugador:
    def __init__(self, nombre, edad, posicion):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.goles = 0

    def registrar_gol(self):
        self.goles += 1

    def __str__(self):
        return f"{self.nombre} ({self.posicion}, {self.edad} años) - Goles: {self.goles}"
