from shared.mysql_connection import select

def validacionIniciarTarea(tarea_id: str) -> bool:
    row = select(
        "SELECT estado FROM Tarea WHERE id = %s AND estado = 'pendiente' LIMIT 1",
        (tarea_id,)
    )
    
    if not row:
        print(f"La tarea {tarea_id} no existe.")
        return False
    else:
        if row[0][0] != 'pendiente':
            print(f"La tarea {tarea_id} no está en estado 'pendiente', no se puede iniciar.")
            return False
        else:
            return True
