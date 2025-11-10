from shared.mysql_connection import commit

def establecerHabitacionPreparada(habitacion_id: int):
    try:
        commit(
            "UPDATE Habitacion SET estado = 'preparada', fecha_habitacion_habilitada = NOW() WHERE id = %s",
            (habitacion_id,)
        )
        print(f"Habitación {habitacion_id} establecida como preparada.")
        return True
    except Exception as e:
        print(f"Error al establecer la habitación como preparada: {e}")
        return False