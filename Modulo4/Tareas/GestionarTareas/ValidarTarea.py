from shared.mysql_connection import commit

def validarTarea(tarea_id: int, estado: str, admin_id: int):
    commit(
        "UPDATE Tarea SET validada = %s, fecha_validacion = NOW(), validado_por_staff_id = %s WHERE id = %s AND NOT estado = 'pendiente'",
        (estado, admin_id, tarea_id)
    )
    print(f"Tarea {tarea_id} validada como {estado} exitosamente.")
    return True