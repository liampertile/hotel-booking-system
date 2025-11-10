from Modulo4.Tareas.ObtenerTareasPorReservaId import obtenerTareasPorReservaId
from Modulo4.ValidacionDeLaHabitacion.EstablecerHabitacionPreparada import establecerHabitacionPreparada
from Modulo4.Tareas.ReestablecerEstadoStaff import reestablecerEstadoStaff 
from shared.obtenerReservaPorId import obtenerReservaPorId

def verificarValidacion(reserva_id: int):
    tareas = obtenerTareasPorReservaId(reserva_id)
    reserva = obtenerReservaPorId(reserva_id)
    if len(tareas) == 0:
        print(f"No hay tareas asociadas a la reserva {reserva_id}.")
        return False
    else:
        for tarea in tareas:
            if tarea['validada'] == 'noValidada' or tarea['fecha_validacion'] > reserva['fecha_check_in']:
                return False
            else:
                continue
        hecho = establecerHabitacionPreparada(reserva['habitacion_id'])
        if hecho:
            print(f"Todas las tareas de la reserva {reserva_id} han sido validadas. Habitación marcada como preparada.")
            hecho = reestablecerEstadoStaff(reserva_id)
            return hecho
        else:
            print(f"No se pudo marcar la habitación de la reserva {reserva_id} como preparada.")
            return False
