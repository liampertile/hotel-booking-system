from shared.mysql_connection import select

def validacionIniciarTarea(tarea_id: str) -> bool:
    row = select(
        "SELECT estado FROM Tarea WHERE id = %s AND estado = 'pendiente' LIMIT 1",
        (tarea_id,)
    )
    
    if not row:
        print(f"La tarea {tarea_id} en estado 'pendiente' no existe.")
        return False
    else:
        return True
