
from Modulo4.ComprobarHabitacion.ComprobarEstado import comprobarEstado
from Modulo4.ComprobarHabitacion.ComprobarReserva import comprobarReserva

def comprobarHabitacion(reserva_id: int):
    habitacionLibre = comprobarEstado(reserva_id)
    if habitacionLibre is None:
        return False
    habitacionReservada = comprobarReserva(reserva_id)
    if habitacionReservada is None:
        return False
    if habitacionLibre and habitacionReservada:
        return True
    else:
        return False