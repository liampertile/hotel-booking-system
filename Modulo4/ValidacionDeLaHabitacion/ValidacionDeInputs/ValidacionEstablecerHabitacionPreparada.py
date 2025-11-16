from shared.mysql_connection import select

def validacionEstablecerHabitacionPreparada(habitacion_id: int) -> bool:
    try:
        habitacion = select(
            "SELECT * FROM Habitacion WHERE id = %s LIMIT 1",
            (habitacion_id,)
        )
        if not habitacion:
            print(f"Habitación con ID {habitacion_id} no encontrada.")
            return False
        else:
            return True
    except Exception as e:
        print(f"Error al validar la habitación: {e}")
        return False