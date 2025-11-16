from Modulo4.Tareas.GestionarTareas.ObtenerTareasPorReservaId import obtenerTareasPorReservaId
from shared.obtenerReservaPorId import obtenerReservaPorId

def validacionCrearTareas(reserva_id: int) -> bool:
    reserva = obtenerReservaPorId(reserva_id)
    if not reserva:
        print(f"La reserva {reserva_id} no existe.")
        return False

    tareas = obtenerTareasPorReservaId(reserva_id)
    
    if len(tareas) == 0:
        return True
    else:
        for tarea in tareas:
            if tarea['estado'] != 'finalizada' and tarea['validada'] == 'noValidada':
                print(f"La tarea {tarea['id']} aún no ha sido finalizada o validada. No se pueden crear nuevas tareas.")
                return False
            continue
    return True