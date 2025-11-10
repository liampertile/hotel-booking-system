from shared.mysql_connection import commit, select

def iniciarTarea(tarea_id: int):
    # ARMAR VALIDACIÓN ANTES DE ENTRAR AL MÓDULO
    row = select(
        "SELECT estado FROM Tarea WHERE id = %s AND estado = 'pendiente' LIMIT 1",
        (tarea_id,)
    )
    
    if not row:
        print(f"La tarea {tarea_id} no existe.")
    else:
        if row[0][0] != 'pendiente':
            print(f"La tarea {tarea_id} no está en estado 'pendiente', no se puede iniciar.")
            # ARMAR VALIDACIÓN ANTES DE ENTRAR AL MÓDULO
        else:
            commit(
                "UPDATE Tarea SET estado = 'enProgreso', fecha_inicio = NOW() WHERE id = %s",
                (tarea_id,)
            )
            print(f"Tarea {tarea_id} iniciada exitosamente.")
            return True
    return False        
    