import sys
import os

# --- Configuración del Path del Proyecto ---
# Esto agrega la carpeta raíz 'hotel-booking-system' al path de Python
# para que podamos importar 'shared' y 'Modulo4' correctamente.
ruta_raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz_proyecto not in sys.path:
    sys.path.append(ruta_raiz_proyecto)
# --- Fin Configuración del Path ---

# Ahora las importaciones de módulos del proyecto funcionarán
from shared.mysql_connection import commit
from shared.obtenerHabitacionByReservaId import obtenerHabitacionPorReservaId
from Modulo4.Tareas.ObtenerTareasPorReservaId import obtenerTareasPorReservaId


def check_in(reserva_id: int):
    """
    Realiza el check-in de una reserva, actualizando el estado de la habitación.
    
    Asume que la reserva ya fue validada (confirmada, fecha OK) 
    por un módulo principal (MAIN) antes de llamar a esta función.
    """
    try:
        # 1. Obtener la habitación y sus tareas usando funciones compartidas
        habitacion = obtenerHabitacionPorReservaId(reserva_id)
        
        # Obtenemos las tareas asociadas a esa reserva
        tareas = obtenerTareasPorReservaId(reserva_id)

        habitacion_id = habitacion['id']
        estado_habitacion = habitacion['estado']

        # 2. Validar estado de la habitación (Regla de negocio del Refinamiento N2)
        if estado_habitacion.lower() != "preparada":
            print(f"Advertencia: Habitación {habitacion_id} no estaba 'preparada'. Forzando estados...")
            
            # 2.1 Para cada tarea no finalizada, marcarla como "mal Finalizado"
            for tarea in tareas:
                # Comprobamos que la tarea exista y tenga estado
                if tarea and tarea.get('estado'):
                    if tarea['estado'].lower() != "finalizado":
                        commit(
                            "UPDATE Tarea SET estado = 'mal Finalizado' WHERE id = %s",
                            (tarea['id'],)
                        )
                        print(f"  - Tarea {tarea['id']} ({tarea.get('descripcion', 'N/A')}) marcada como 'mal Finalizado'.")
            
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
            print(f"\n✅ Check-in realizado con éxito.")
            print(f"Habitación {habitacion_id} (Reserva {reserva_id}) marcada como 'ocupada'.")
        else:
            # Esto podría pasar si el estado ya era 'ocupada' o si hay un problema de BD
            print(f"Error: No se pudo actualizar la habitación {habitacion_id} a 'ocupada'.")

    except Exception as err:
        print(f"Error inesperado durante el check-in (reserva {reserva_id}): {err}")

# --- Bloque de prueba ---
if __name__ == "__main__":
    """
    Permite ejecutar este módulo directamente para probar el check-in.
    Ejemplo de uso desde la terminal (estando en la carpeta raíz del proyecto):
    python -m Modulo5.modulo5
    """
    try:
        # Asumimos que mysql_connection.py está configurado y la BD existe.
        reserva_id_test = int(input("Ingrese el ID de la reserva para hacer Check-in: "))
        check_in(reserva_id_test)
    except ValueError:
        print("Error: El ID debe ser un número entero.")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")