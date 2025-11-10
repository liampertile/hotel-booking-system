from shared.mysql_connection import select

def validacionValidarTarea(tarea_id: str, admin_id: int) -> bool:
    admin = select(
        "SELECT tipo FROM Persona WHERE id = %s AND tipo = 'administracion' LIMIT 1",
        (admin_id,)
    )
    
    if not admin:
        print(f"El usuario {admin_id} no tiene permisos de administración.")
        return False
    
    row = select(
        "SELECT estado FROM Tarea WHERE id = %s AND estado = 'finalizada' AND validado_por_staff_id IS NULL LIMIT 1",
        (tarea_id,)
    )
    
    if not row:
        print(f"La tarea {tarea_id} en estado 'finalizada' no existe.")
        return False
    else:
        return True