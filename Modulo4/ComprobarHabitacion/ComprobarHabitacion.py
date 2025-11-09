
from Modulo4.ComprobarHabitacion.ComprobarEstado import comprobarEstado
from Modulo4.ComprobarHabitacion.ComprobarReserva import comprobarReserva

def comprobarHabitacion(reserva_id: int):
    habitacionLibre = comprobarEstado(reserva_id)
    if habitacionLibre is None:
        return None
    habitacionReservada = comprobarReserva(reserva_id)
    if habitacionReservada is None:
        return None
    if habitacionLibre and habitacionReservada:
        print("La habitación debe ser preparada")   
        return True
    else:
        print("La habitación no se encuentra habilitada para ser preparada")
        return False