import sys
from os.path import abspath, dirname
from shared.mysql_connection import select, commit

from typing import List, Dict, Any

def _obtener_habitacion_y_tareas(reserva_id: int) -> Dict[str, Any]:
    """
    Función interna para obtener la habitación y sus tareas asociadas 
    a través de la reserva.
    """
    # Obtenemos la habitación primero
    habitacion_rows = select(
       "SELECT h.id, h.estado "
       "FROM Habitacion AS h "
       "JOIN Reserva r ON h.id = r.habitacion_id "
       "WHERE r.id = %s "
       "LIMIT 1",
       (reserva_id,)
    )
    
    if not habitacion_rows:
        return None  # No se encontró habitación para esa reserva

    habitacion_id, habitacion_estado = habitacion_rows[0]
    
    # Obtenemos las tareas de esa reserva
    tarea_rows = select(
        "SELECT id, estado FROM Tarea WHERE reserva_id = %s",
        (reserva_id,)
    )
    
    tareas = []
    for tarea_row in tarea_rows:
        tareas.append({"id": tarea_row[0], "estado": tarea_row[1]})
        
    return {
        "id": habitacion_id,
        "estado": habitacion_estado,
        "tareas": tareas
    }

def check_in(reserva_id: int):
    """
    Realiza el check-in de una reserva, actualizando el estado de la habitación.
    
    Asume que la reserva ya fue validada (confirmada, fecha OK) por el módulo MAIN.
    """
    try:
        # 1. Obtener la habitación y sus tareas
        datos = _obtener_habitacion_y_tareas(reserva_id)
        
        if not datos:
            print(f"Error: No se encontró habitación para la reserva {reserva_id}.")
            return

        habitacion_id = datos['id']
        estado_habitacion = datos['estado']
        tareas = datos['tareas']

        # 2. Validar estado de la habitación (Regla de negocio)
        if estado_habitacion.lower() != "preparada":
            print(f"Advertencia: Habitación {habitacion_id} no estaba 'preparada'. Forzando estados...")
            
            # 2.1 Para cada tarea no finalizada, marcarla como "mal Finalizado"
            for tarea in tareas:
                if tarea['estado'].lower() != "finalizado":
                    commit(
                        "UPDATE Tarea SET estado = 'mal Finalizado' WHERE id = %s",
                        (tarea['id'],)
                    )
                    print(f"  - Tarea {tarea['id']} marcada como 'mal Finalizado'.")
            
            # 2.2 Marcar habitación como "preparada" para poder continuar
            commit(
                "UPDATE Habitacion SET estado = 'preparada' WHERE id = %s",
                (habitacion_id,)
            )
            print(f"Habitación {habitacion_id} forzada a estado 'preparada'.")

        # 3. Registrar Ocupación
        # En este punto, la habitación SIEMPRE está 'preparada' (sea originalmente o forzada)
        affected = commit(
            "UPDATE Habitacion SET estado = 'ocupada' WHERE id = %s",
            (habitacion_id,)
        )

        if affected > 0:
            print(f"\nCheck-in realizado con éxito.")
            print(f"Habitación {habitacion_id} (Reserva {reserva_id}) marcada como 'ocupada'.")
        else:
            print(f"Error: No se pudo actualizar la habitación {habitacion_id} a 'ocupada'.")

    except Exception as err:
        print(f"Error inesperado durante el check-in: {err}")

# Bloque de prueba
if __name__ == "__main__":
    try:
        # Asumimos que mysql_connection.py está configurado y la BD existe.
        reserva_id_test = int(input("Ingrese el ID de la reserva para hacer Check-in: "))
        check_in(reserva_id_test)
    except ValueError:
        print("Error: El ID debe ser un número entero.")