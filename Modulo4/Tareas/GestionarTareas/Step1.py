from Modulo4.Tareas.GestionarTareas.ObtenerTareasPorReservaId import obtenerTareasPorReservaId
from Modulo4.Tareas.GestionarTareas.Step2 import step2

def step1(reserva_id: int, admin_id: int = 2):
    try:
        while True:
            tareas = obtenerTareasPorReservaId(reserva_id)
            if len(tareas) == 0:
                print("No hay tareas para gestionar.")
                return
            else:
                print("\n|-------| Tareas asociadas a la reserva |-------|\n")
                for tarea in tareas:
                    print(f"    TAREA {tarea['id']}: {tarea['descripcion']} - Estado: {tarea['estado']} - Validada: {tarea['validada']}")
                print("\n|-----------------------------------------------|\n\n")
                ingreso = input("Seleccione la tarea que desea gestionar ingresando su ID o 'q' para salir: ")
                if ingreso.lower() == 'q':
                    print("Saliendo de la gestión de tareas.")
                    return
                else:
                    try:
                        tarea_id = int(ingreso)
                    except ValueError:
                        print("ID de tarea inválido. Por favor, ingrese un número entero.")
                        continue
                if not any(tarea['id'] == tarea_id for tarea in tareas):
                    print(f"No existe una tarea con ID {tarea_id} para esta reserva.")
                    continue
                
                step2(tarea_id, admin_id)
    except KeyboardInterrupt:
        print("\nGestión de tareas interrumpida por el usuario.")
        