import sys
import os

# --- Configuración del Path ---
ruta_raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz_proyecto not in sys.path:
    sys.path.append(ruta_raiz_proyecto)
# --- Fin Configuración del Path ---

from shared.mysql_connection import commit
from shared.obtenerHabitacionByReservaId import obtenerHabitacionPorReservaId

# --- Imports de Funciones de Módulo 4 ---
from Modulo4.Tareas.GestionarTareas.ObtenerTareasPorReservaId import obtenerTareasPorReservaId
from Modulo4.Tareas.GestionarTareas.FinalizarTarea import finalizarTarea
from Modulo4.Tareas.GestionarTareas.ValidarTarea import validarTarea
from Modulo4.Tareas.ReestablecerEstadoStaff import reestablecerEstadoStaff
from Modulo4.ValidacionDeLaHabitacion.EstablecerHabitacionPreparada import establecerHabitacionPreparada
# --- Fin de Imports de Módulo 4 ---


def check_in(reserva_id: int, admin_id: int):
    """
    Realiza el check-in de una reserva.
    Llama a las funciones de Módulo 4 para forzar estados si es necesario.
    """
    try:
        # 1. Obtener la habitación y sus tareas
        habitacion = obtenerHabitacionPorReservaId(reserva_id)
        
        if not habitacion:
            print(f"Error (Módulo 5): No se encontró habitación para la reserva {reserva_id}.")
            return

        tareas = obtenerTareasPorReservaId(reserva_id)
        habitacion_id = habitacion['id']
        estado_habitacion = habitacion['estado']

        # 2. Validar estado de la habitación
        if estado_habitacion.lower() != "preparada":
            print(f"Advertencia: La habitación {habitacion_id} no estaba preparada. Registrando incumplimiento...")
            
            staff_fue_liberado = False

            # 2.1 Forzar tareas usando funciones de Módulo 4
            for tarea in tareas:
                if tarea and tarea.get('estado') and tarea['estado'].lower() != "finalizado":
                    
                    tarea_id = tarea['id']
                    print(f"  - Terminando la tarea {tarea_id}...")
                    finalizarTarea(tarea_id)
                    
                    print(f"  - la tarea {tarea_id} fue validada como Mal Realizada por Admin {admin_id}...")
                    validarTarea(tarea_id, 'malHecha', admin_id)
                    
                    if not staff_fue_liberado and tarea.get('staff_asignado_id'):
                        print(f"  - Liberando al staff {tarea.get('staff_asignado_id')}...")
                        reestablecerEstadoStaff(tarea_id) 
                        staff_fue_liberado = True

            # 2.2 Marcar habitación como "preparada" (usando Módulo 4)
            print(f"Forzando estado de Habitación {habitacion_id} a 'preparada'.")
            establecerHabitacionPreparada(habitacion_id)
            # --- FIN DEL CAMBIO ---

        # 3. Registrar Ocupación
        affected = commit(
            "UPDATE Habitacion SET estado = 'ocupada' WHERE id = %s",
            (habitacion_id,)
        )

        if affected > 0:
            print(f"\n✅ Check-in realizado con éxito.")
            print(f"Habitación {habitacion_id} (Reserva {reserva_id}) marcada como 'ocupada'.")
        else:
            print(f"Error: No se pudo actualizar la habitación {habitacion_id} a 'ocupada'.")

    except Exception as err:
        print(f"Error inesperado durante el check-in (reserva {reserva_id}): {err}")

# --- (El bloque de prueba queda igual) ---
if __name__ == "__main__":
    try:
        reserva_id_test = int(input("Ingrese el ID de la reserva para hacer Check-in: "))
        admin_id_test = int(input("Ingrese el ID de admin que realiza la operación: "))
        check_in(reserva_id_test, admin_id_test)
    except ValueError:
        print("Error: Los IDs deben ser números enteros.")

