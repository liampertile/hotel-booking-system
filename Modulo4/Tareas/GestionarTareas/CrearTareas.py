from shared.mysql_connection import commit

TAREAS = ["limpieza", "reposición", "mantenimiento"]

def crearTareas(reserva_id: int):
    try:
        for tarea in TAREAS:
            print(f"Creando tarea de {tarea} para la reserva {reserva_id}")
            commit(
                "INSERT INTO Tarea (reserva_id, descripcion) VALUES (%s, %s)",
                (reserva_id, tarea)
            )
        return True
    except Exception:
        return False