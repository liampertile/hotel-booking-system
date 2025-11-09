from shared.mysql_connection import select

def obtenerTareasPorReservaId(reserva_id: int):
    tareas = select(
        "SELECT * FROM Tarea WHERE reserva_id = %s",
        (reserva_id,)
    )
    if tareas is None or len(tareas) == 0:
        print(f"No se encontraron tareas para la reserva {reserva_id}")
        return []
    else:
        formatted_tareas = []
        for tarea in tareas:
            formatted_tareas.append({
                "id": tarea[0],
                "reserva_id": tarea[1],
                "descripcion": tarea[2],
                "estado": tarea[3],
                "fecha_asignacion": tarea[4],
                "fecha_inicio": tarea[5],
                "fecha_fin": tarea[6],
                "fecha_validacion": tarea[7],
                "validada": tarea[8],
                "staff_asignado_id": tarea[9],
                "validado_por_staff_id": tarea[10]
            })
        return formatted_tareas