from shared.obtenerHabitacionByReservaId import obtenerHabitacionPorReservaId

def comprobarEstado(reserva_id: int):
    habitacion = obtenerHabitacionPorReservaId(reserva_id)
    if habitacion is None:
        print("La habitación no existe.")
        return None
    else:
        if habitacion["estado"] == "libre":
            print(f"\nLa habitación {habitacion['id']} se encuentra libre.")
            return True
        else:
            print(f"\nLa habitación {habitacion['id']} no se encuentra libre.")
            return False