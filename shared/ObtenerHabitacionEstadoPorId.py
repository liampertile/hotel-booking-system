from shared.mysql_connection import select

def obtenerEstadoHabitacionPorId(habitacion_id: int):
    habitacionEstado = select(
        "SELECT estado FROM habitacion WHERE id = %s", (habitacion_id,)
    )
    
    if habitacionEstado:
        return habitacionEstado[0][0]
    else:
        return None