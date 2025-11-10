from shared.mysql_connection import select, commit

def reestablecerEstadoStaff(tarea_id: int):
    try:
        staff_asignado_id = select(
            "SELECT staff_asignado_id FROM Tarea WHERE id = %s LIMIT 1",
            (tarea_id,)
        )
        print(F"staff_asignado_id[0][0] {staff_asignado_id[0][0]}")
        if staff_asignado_id[0][0]:
            commit(
                "UPDATE Persona SET ocupado = 0 WHERE id = %s and tipo = 'limpieza'",
                (staff_asignado_id[0][0],)
            )
            print(f"EL staff con ID {staff_asignado_id[0][0]} ya no se encuentra ocupado.")
            return True
        else:
            print(f"No se encontró staff asignado para la tarea {tarea_id}.")
            return False
    except:
        print("ERROR ERROR ERROR")