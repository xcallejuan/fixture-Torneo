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

class Torneo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.equipos = []

    def registrar_equipo(self, equipo):
        self.equipos.append(equipo)

    def mostrar_equipos(self):
        print(f"\nEquipos inscritos en el torneo '{self.nombre}':")
        for equipo in self.equipos:
            print("-", equipo)

if __name__ == "__main__":
    torneo = Torneo("Copa Universitaria", "Eliminación Directa")

    equipo1 = Equipo("Tigres", "Medellín")
    equipo2 = Equipo("Leones", "Bogotá")
    equipo1.agregar_jugador(Jugador("Juan Pérez", 20, "Delantero"))
    equipo1.agregar_jugador(Jugador("Carlos López", 22, "Portero"))




