# Definición de la clase Player
class Player:
    def __init__(self, name, health=100, points=0):
        self.name = name  # Nombre del jugador
        self.health = health  # Nivel de salud del jugador
        self.points = points  # Puntos acumulados por el jugador

    def ganarPuntos(self, amount):
        """ Método para que el jugador gane puntos """
        self.points += amount
        print(f"{self.name} ha ganado {amount} puntos. Puntos totales: {self.points}")

    def hacerDaño(self, damage):
        """ Método para que el jugador reciba daño """
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} ha sido derrotado!")
        else:
            print(f"{self.name} ha recibido {damage} de daño. Salud restante: {self.health}")


# Ejemplo
if __name__ == "__main__":
    # Creamos dos jugadores
    player1 = Player("Jugador 1")
    player2 = Player("Jugador 2", health=150, points=500)

    # Simulamos una batalla
    player1.ganarPuntos(50)
    player2.hacerDaño(20)
    player1.hacerDaño(30)
    player2.ganarPuntos(100)

    # Mostramos información final de los jugadores
    print("\nInformación final de los jugadores:")
    print(f"{player1.name}: Salud = {player1.health}, Puntos = {player1.points}")
    print(f"{player2.name}: Salud = {player2.health}, Puntos = {player2.points}")
