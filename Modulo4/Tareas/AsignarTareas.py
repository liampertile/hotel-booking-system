from Modulo4.Tareas.ObtenerTareasPorReservaId import obtenerTareasPorReservaId
from Modulo4.shared.ObtenerPersonalLimpiezaLibre import obtenerPersonalLimpiezaLibre
from shared.mysql_connection import commit

def asignarTareas(reserva_id: int):
    tareas = obtenerTareasPorReservaId(reserva_id)
    if len(tareas) == 0:
        print("No hay tareas para asignar.")
        return
    else:
        personalDisponibleId = obtenerPersonalLimpiezaLibre()
        for tarea in tareas:
            print("tarea['id']:", tarea['id'], "tarea['estado']:", tarea['estado'])
            if tarea['estado'] != 'pendiente':
                print(f"La tarea {tarea['id']} ya fue procesada, se omite.")
                continue
            if tarea['staff_asignado_id'] is not personalDisponibleId:
                print("La tarea ya se encuentra asignada a otro personal, se omite.")
                continue
            print(f"Asignando tarea {tarea['id']} de {tarea['descripcion']} para la reserva {reserva_id}")
            commit("UPDATE Tarea SET fecha_asignacion = NOW(), staff_asignado_id = %s WHERE id = %s",
                   (personalDisponibleId, tarea['id']))
            commit("UPDATE Persona SET ocupado = 1 WHERE id = %s",
                   (personalDisponibleId,))
    