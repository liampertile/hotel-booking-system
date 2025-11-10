from shared.obtenerReservaPorId import obtenerReservaPorId

def validarExisteReservaPorId(reserva_id: int) -> bool:
    reserva = obtenerReservaPorId(reserva_id)
    if reserva is None:
        print(f"Reserva confirmada con ID {reserva_id} no encontrada.")
        return False
    return True