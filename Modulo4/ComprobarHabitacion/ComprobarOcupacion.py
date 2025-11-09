
from shared.obtenerHabitacionByReservaId import obtenerHabitacionPorReservaId

def comprobarOcupacion(reserva_id: int):
    habitacion = obtenerHabitacionPorReservaId(reserva_id)
    if habitacion is None:
        print("La habitación no existe.")
        return None
    else:
        if habitacion["estado"] == "ocupada":
            print(f"La habitación {habitacion['numero']} está ocupada.")
            return True
        else:
            print(f"La habitación {habitacion['numero']} no está ocupada.")
            return False

