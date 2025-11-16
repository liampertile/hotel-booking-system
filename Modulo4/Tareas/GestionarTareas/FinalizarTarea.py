from shared.mysql_connection import commit

def finalizarTarea(tarea_id: int):
    commit(
        "UPDATE Tarea SET estado = 'finalizada', fecha_fin = NOW() WHERE id = %s",
        (tarea_id,)
    )
    print(f"Tarea {tarea_id} finalizada exitosamente.")
    return True