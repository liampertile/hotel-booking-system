from shared.mysql_connection import select

def validacionIniciarTarea(tarea_id: str) -> bool:
    row = select(
        "SELECT staff_asignado_id FROM Tarea WHERE id = %s AND estado = 'pendiente' LIMIT 1",
        (tarea_id,)
    )
    
    if not row:
        print(f"La tarea {tarea_id} no se encuentra pendiente de iniciar.")
        return False
    else:
        if row[0][0] is None:
            print(f"La tarea {tarea_id} no tiene un staff asignado, no se puede iniciar.")
            return False
        else:
            return True
