from shared.obtenerReservaPorId import obtenerReservaPorId
from datetime import datetime

def comprobarReserva(reserva_id: int):
    reserva = obtenerReservaPorId(reserva_id)
    if reserva is None:
        print("La reserva no existe.")
        return None
    else:
        checkin = reserva["fecha_check_in"]
        estado = reserva["estado"]
        today = datetime.now()
        if checkin > today and estado == "confirmada":
            print("La habitación tiene una próxima reserva")
            return True
        else:
            print("La habitación no tiene una próxima reserva")
            return False
        
        