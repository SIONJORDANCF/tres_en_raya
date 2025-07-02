def imprimir_tablero(tablero):
    print()
    for i in range(3):
        fila = " | ".join(tablero[i*3:(i+1)*3])
        print(fila)
        if i < 2:
            print("-" * 9)
    print()

def verificar_ganador(tablero, jugador):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    return any(all(tablero[i] == jugador for i in combo) for combo in combinaciones)

def tablero_lleno(tablero):
    return all(casilla != " " for casilla in tablero)

def jugar():
    tablero = [" "] * 9
    jugador_actual = "X"
    
    while True:
        imprimir_tablero(tablero)
        try:
            movimiento = int(input(f"Turno de {jugador_actual}. Elige una posición (1-9): ")) - 1
            if tablero[movimiento] != " ":
                print("Esa posición ya está ocupada. Intenta otra.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida. Debes ingresar un número del 1 al 9.")
            continue

        tablero[movimiento] = jugador_actual

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Felicidades! {jugador_actual} ha ganado.")
            break
        elif tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break
        else:
            jugador_actual = "O" if jugador_actual == "X" else "X"

# Ejecutar el juego
if __name__ == "__main__":
    jugar()