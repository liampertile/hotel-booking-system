from shared.mysql_connection import select

def validacionFinalizarTarea(tarea_id: int) -> bool:
    row = select(
        "SELECT estado FROM Tarea WHERE id = %s AND estado = 'enProgreso' LIMIT 1",
        (tarea_id,)
    )
    
    if not row:
        print(f"La tarea {tarea_id} no se encuentra en progreso, no se puede finalizar.")
        return False
    else:
        if row[0][0] != 'enProgreso':
            print(f"La tarea {tarea_id} no está en estado 'enProgreso', no se puede finalizar.")
            return False
        else:
            return True
    