from shared.mysql_connection import select


def validacionTareasCreadasPendientes(reserva_id: int) -> bool:
    row = select(
        "SELECT id FROM Tarea WHERE reserva_id = %s AND estado = 'pendiente'",
        (reserva_id,)
    )
    
    if not row:
        print(f"No hay tareas pendientes creadas para la reserva {reserva_id}.")
        return False
    else:
        return True