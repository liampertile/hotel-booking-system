from shared.mysql_connection import select

def validar_checkout(reserva_id: int):
    """
    Valida precondiciones necesarias para ejecutar un CHECK-OUT:
      ✔ La reserva debe existir
      ✔ La reserva debe estar en estado 'confirmada'
      ✔ La habitación asociada debe estar 'ocupada'
    Devuelve:
      - (True, habitacion_id) si todo está OK
      - (False, None) si hay error
    """

    # 1 - Validar tipo de dato
    if not isinstance(reserva_id, int) or reserva_id <= 0:
        print("Error: el ID de reserva debe ser un número entero positivo.")
        return False, None

    # 2 - Traer la reserva
    res = select("SELECT habitacion_id, estado FROM Reserva WHERE id = %s", (reserva_id,))
    if not res:
        print("Error: la reserva no existe.")
        return False, None

    habitacion_id, estado_reserva = res[0]

    # 3 - Validar estado de la reserva
    if estado_reserva.lower() != "confirmada":
        print(f"Error: la reserva {reserva_id} no está confirmada (estado actual: {estado_reserva}).")
        return False, None

    # 4 - Validar estado de la habitación
    hab = select("SELECT estado FROM Habitacion WHERE id = %s", (habitacion_id,))
    if not hab:
        print("Error: la habitación asociada no existe.")
        return False, None

    estado_habitacion = hab[0][0]

    if estado_habitacion.lower() != "ocupada":
        print(f"Error: la habitación {habitacion_id} no se encuentra ocupada (estado actual: {estado_habitacion}).")
        return False, None

    return True, habitacion_id
