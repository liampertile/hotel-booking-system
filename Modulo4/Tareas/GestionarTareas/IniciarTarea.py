from shared.mysql_connection import commit

def iniciarTarea(tarea_id: int):
    commit(
        "UPDATE Tarea SET estado = 'enProgreso', fecha_inicio = NOW() WHERE id = %s",
        (tarea_id,)
    )
    print(f"Tarea {tarea_id} iniciada exitosamente.")
    return True