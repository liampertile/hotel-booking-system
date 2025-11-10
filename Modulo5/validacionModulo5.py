import sys
import os
from datetime import datetime

# --- Configuración del Path del Proyecto ---
# Esto agrega la carpeta raíz 'hotel-booking-system' al path
ruta_raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz_proyecto not in sys.path:
    sys.path.append(ruta_raiz_proyecto)
# --- Fin Configuración del Path ---

from shared.obtenerReservaPorId import obtenerReservaPorId
from shared.obtenerHabitacionByReservaId import obtenerHabitacionPorReservaId

def validar_checkin(reserva_id: int) -> bool:
    """
    Verifica las precondiciones de negocio ANTES de llamar al Módulo 5 (check_in).
    
    Reglas (según pseudocódigo + validación extra):
    1. La reserva debe existir.
    2. La reserva debe estar en estado "confirmada".
    3. La fecha actual debe ser >= a la fecha_check_in.
    """
    
    # --- 1. & 2. Validar estado de la reserva ---
    reserva = obtenerReservaPorId(reserva_id)
    
    if not reserva:
        print(f"Error (Validación): La reserva {reserva_id} no existe.")
        return False

    if reserva['estado'].lower() != "confirmada":
        print(f"Error (Validación): La reserva {reserva_id} no está 'confirmada'.")
        print(f"  (Estado actual: {reserva['estado']})")
        return False

    # --- 3. Validar Fecha ---
    # Usamos .date() para comparar solo el día, ignorando la hora
    fecha_actual = datetime.now().date()
    fecha_check_in = reserva['fecha_check_in'].date()

    if fecha_actual < fecha_check_in:
        print(f"Error (Validación): Aún no es la fecha de check-in.")
        print(f"  (Hoy: {fecha_actual} | Check-in: {fecha_check_in})")
        return False


    # Si pasa todas las validaciones:
    print(f"Validación de Check-in (Reserva {reserva_id}): OK.")
    return True

# --- Bloque de prueba ---
if __name__ == "__main__":
    """
    Permite probar esta validación de forma aislada.
    Uso: python -m validaciones.validar_checkin
    """
    try:
        reserva_id_test = int(input("Ingrese el ID de la reserva a VALIDAR para Check-in: "))
        
        if validar_checkin(reserva_id_test):
            print("\nResultado: SÍ, se puede hacer check-in.")
        else:
            print("\nResultado: NO, no se puede hacer check-in.")
            
    except ValueError:
        print("Error: El ID debe ser un número entero.")