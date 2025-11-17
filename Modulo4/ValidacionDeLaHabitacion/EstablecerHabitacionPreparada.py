from shared.mysql_connection import commit
from shared.ObtenerHabitacionEstadoPorId import obtenerEstadoHabitacionPorId

def establecerHabitacionPreparada(habitacion_id: int):
    try:
        habitacionEstado =  obtenerEstadoHabitacionPorId(habitacion_id)
        if habitacionEstado == 'ocupada':
            print(f"La habitación {habitacion_id} está ocupada y no se puede marcar como preparada.")
            return False
        else:
            commit(
                "UPDATE Habitacion SET estado = 'preparada', fecha_habitacion_habilitada = NOW() WHERE id = %s and not estado = 'ocupada' ",
                (habitacion_id,)
            )
            print(f"Habitación {habitacion_id} establecida como preparada.")
            return True
    except Exception as e:
        print(f"Error al establecer la habitación como preparada: {e}")
        return False