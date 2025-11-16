import sys
import os
from datetime import datetime

# Agregar raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shared.mysql_connection import select, commit
from validacionModulo6 import validar_checkout
from Modulo4.modulo4 import prepararHabitacion


def check_out(reserva_id: int):
    """
    MÓDULO 6 — CHECK-OUT
    Flujo:
      1. Validaciones del negocio (reserva y habitación)
      2. Cambiar habitación → libre
      3. Cambiar reserva → finalizada
      4. Ejecutar preparación (módulo 4)
      5. Registrar hora de check-out
    """

    ok, habitacion_id = validar_checkout(reserva_id)
    if not ok:
        return  # Las validaciones ya mostraron el error correspondiente

    # ------------------------------------------------------------------
    # 1) LIBERAR HABITACIÓN
    # ------------------------------------------------------------------
    try:
        filas = commit("""
            UPDATE Habitacion
            SET estado = 'libre'
            WHERE id = %s
        """, (habitacion_id,))

        if filas == 0:
            print("Error al liberar la habitación (no se modificó ninguna fila).")
            return

    except Exception as e:
        print("Error al liberar la habitación:", e)
        return

    # ------------------------------------------------------------------
    # 2) FINALIZAR RESERVA
    # ------------------------------------------------------------------
    try:
        ahora = datetime.now()

        filas = commit("""
            UPDATE Reserva
            SET estado = 'finalizada',
                fecha_check_out = %s
            WHERE id = %s
        """, (ahora, reserva_id))

        if filas == 0:
            print("Error al finalizar la reserva.")
            return

    except Exception as e:
        print("Error al actualizar la reserva:", e)
        return

    # ------------------------------------------------------------------
    # 3) PREPARAR HABITACIÓN (Módulo 4)
    # ------------------------------------------------------------------
    try:
        prepararHabitacion(reserva_id, habitacion_id)
    except Exception as e:
        print("Advertencia: la preparación falló o no pudo completarse:", e)

    # ------------------------------------------------------------------
    # 4) MENSAJE FINAL
    # ------------------------------------------------------------------
    print("\n✔ CHECK-OUT realizado correctamente.")
    print(f"Reserva finalizada: {reserva_id}")
    print(f"Habitación liberada: {habitacion_id}")
    print(f"Hora del check-out: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")
if __name__ == "__main__":
    try:
        reserva_id = int(input("Ingrese el ID de la reserva para check-out: "))
        check_out(reserva_id)
    except ValueError:
        print("Debe ingresar un número entero.")
