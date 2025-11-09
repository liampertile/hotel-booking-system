from Modulo4.Tareas.ObtenerTareasPorReservaId import obtenerTareasPorReservaId
from Modulo4.Tareas.GestionarTareas.IniciarTarea import iniciarTarea
from Modulo4.Tareas.GestionarTareas.FinalizarTarea import finalizarTarea

from Modulo4.Tareas.ValidacionDeInputs.ValidacionIniciarTarea import validacionIniciarTarea
from Modulo4.Tareas.ValidacionDeInputs.ValidacionFinalizarTarea import validacionFinalizarTarea

def gestionarTareas(reserva_id: int):
    tareas = obtenerTareasPorReservaId(reserva_id)
    if len(tareas) == 0:
        print("No hay tareas para gestionar.")
        return
    for tarea in tareas:
        print(f"GESTIÓN DE TAREA {tarea['id']}")
        print("Ingrese el número de opción según corresponda:")
        print("1. Iniciar tarea")
        print("2. Finalizar tarea")
        opcion = input("Opción: ")
        match opcion:
            case '1':
                avanzar = validacionIniciarTarea(tarea['id'])
                if avanzar:
                    iniciarTarea(tarea['id'])
                else:
                    print("No se pudo iniciar la tarea debido a la validación.")
            case '2':
                avanzar = validacionFinalizarTarea(tarea['id'])
                if avanzar:
                    finalizarTarea(tarea['id'])
                else:
                    print("No se pudo finalizar la tarea debido a la validación.")