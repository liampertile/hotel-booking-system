import sys
import os

# --- Configuración del Path ---
ruta_raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz_proyecto not in sys.path:
    sys.path.append(ruta_raiz_proyecto)
# --- Fin Configuración del Path ---

from shared.mysql_connection import commit, select
from shared.obtenerHabitacionByReservaId import obtenerHabitacionPorReservaId
from shared.obtenerReservaPorId import obtenerReservaPorId # <--- IMPORT NECESARIO

# --- Imports de Funciones de Módulo 4 ---
from Modulo4.Tareas.GestionarTareas.ObtenerTareasPorReservaId import obtenerTareasPorReservaId
from Modulo4.Tareas.GestionarTareas.FinalizarTarea import finalizarTarea
from Modulo4.Tareas.GestionarTareas.ValidarTarea import validarTarea
from Modulo4.Tareas.ReestablecerEstadoStaff import reestablecerEstadoStaff
from Modulo4.ValidacionDeLaHabitacion.EstablecerHabitacionPreparada import establecerHabitacionPreparada
# --- Fin de Imports de Módulo 4 ---

def _obtener_datos_cliente(cliente_id: int):
    """Busca datos básicos del cliente para mostrar en el resumen."""
    rows = select("SELECT nombre, dni, email FROM Persona WHERE id = %s", (cliente_id,))
    if rows:
        return {"nombre": rows[0][0], "dni": rows[0][1], "email": rows[0][2]}
    return {"nombre": "Desconocido", "dni": "N/A", "email": "N/A"}


def _mostrar_resumen(reserva, habitacion, cliente):
    """Imprime la ficha de datos para confirmar."""
    print("\n" + "="*50)
    print(f"       CONFIRMACIÓN DE CHECK-IN")
    print("="*50)
    print(f" RESERVA ID:      {reserva['id']}")
    print(f" ESTADO ACTUAL:   {reserva['estado'].upper()}")
    print("-" * 50)
    print(f" HUÉSPED:         {cliente['nombre']}")
    print(f" DNI:             {cliente['dni']}")
    print(f" EMAIL:           {cliente['email']}")
    print("-" * 50)
    print(f" HABITACIÓN:      {habitacion['id']}")
    print(f" ESTADO HAB.:     {habitacion['estado'].upper()}")
    print(f" CAPACIDAD:       {habitacion['capacidad']} personas")
    print("-" * 50)
    print(f" CHECK-IN:        {reserva['fecha_check_in']}")
    print(f" CHECK-OUT:       {reserva['fecha_check_out']}")
    print("="*50 + "\n")

    
def check_in(reserva_id: int, admin_id: int):
    """
    Realiza el check-in de una reserva.
    Llama a las funciones de Módulo 4 para forzar estados si es necesario.
    """
    try:
        reserva = obtenerReservaPorId(reserva_id)
        if not reserva:
            print(f"Error: La reserva {reserva_id} no existe.")
            return
        
        # 1. Obtener la habitación y sus tareas
        habitacion = obtenerHabitacionPorReservaId(reserva_id)
        
        if not habitacion:
            print(f"Error (Módulo 5): No se encontró habitación para la reserva {reserva_id}.")
            return

        cliente = _obtener_datos_cliente(reserva['cliente_id'])

        _mostrar_resumen(reserva, habitacion, cliente)

        while True:
            confirmacion = input("¿Los datos son correctos y desea proceder con el Check-in? (s/n): ").lower().strip()
            if confirmacion == 'n':
                print("Operación cancelada por el usuario.")
                return
            elif confirmacion == 's':
                break
            else:
                print("Opción inválida. Ingrese 's' para sí o 'n' para no.")


        tareas = obtenerTareasPorReservaId(reserva_id)
        if len(tareas) == 0:
            print(f"No hay tareas asociadas a la reserva {reserva_id}.")
            return False
        habitacion_id = habitacion['id']
        estado_habitacion = habitacion['estado']

        # 2. Validar estado de la habitación
        if estado_habitacion.lower() != "preparada":
            print(f"Advertencia: La habitación {habitacion_id} no estaba preparada. Registrando incumplimiento...")
            
            staff_fue_liberado = False

            # 2.1 Forzar tareas usando funciones de Módulo 4
            for tarea in tareas:
                if tarea and tarea.get('estado') and tarea['estado'].lower() != "finalizada":
                    
                    tarea_id = tarea['id']
                    # print(f"  - Terminando la tarea {tarea_id}...")
                    finalizarTarea(tarea_id)
                    
                    # print(f"  - la tarea {tarea_id} fue validada como Mal Realizada por Admin {admin_id}...")
                    validarTarea(tarea_id, 'malHecha', admin_id)
                    
            if not staff_fue_liberado and tarea.get('staff_asignado_id'):
                # print(f"  - Liberando al staff {tarea.get('staff_asignado_id')}...")
                reestablecerEstadoStaff(tarea_id) 
                staff_fue_liberado = True

            # 2.2 Marcar habitación como "preparada" (usando Módulo 4)
            print(f"Forzando estado de Habitación {habitacion_id} a preparada.")
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

