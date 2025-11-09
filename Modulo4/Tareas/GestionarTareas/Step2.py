from Modulo4.Tareas.ValidacionDeInputs.ValidacionIniciarTarea import validacionIniciarTarea
from Modulo4.Tareas.ValidacionDeInputs.ValidacionFinalizarTarea import validacionFinalizarTarea
from Modulo4.Tareas.GestionarTareas.IniciarTarea import iniciarTarea
from Modulo4.Tareas.GestionarTareas.FinalizarTarea import finalizarTarea

def step2(tarea_id: str):
    
    while True:
        print(f"\n|---------| GESTIÓN DE TAREA {tarea_id} |---------|\n")
        print(" Ingrese el número de opción según corresponda:")
        print(" 1. Iniciar tarea")
        print(" 2. Finalizar tarea")
        print(" 0. Volver al menú anterior\n")
        print("|---------------------------------------------|\n\n")
        opcion = input("Opción: ")
        
        if opcion == '0':
            return
        else:
            match opcion:
                case '1':
                    avanzar = validacionIniciarTarea(tarea_id)
                    if avanzar:
                        hecho = iniciarTarea(tarea_id)
                        if hecho:
                            print("Tarea iniciada correctamente.")
                            return
                        else:
                            print("No se pudo iniciar la tarea.")
                    else:
                        print("VALIDACIÓN FALLIDA: No se pudo iniciar la tarea.")
                case '2':
                    avanzar = validacionFinalizarTarea(tarea_id)
                    if avanzar:
                        hecho = finalizarTarea(tarea_id)
                        if hecho:
                            print("Tarea finalizada correctamente.")
                            return
                        else:
                            print("No se pudo finalizar la tarea.")
                    else:
                        print("VALIDACIÓN FALLIDA: No se pudo finalizar la tarea.")
                case _:
                    print("Opción inválida. Por favor, ingrese una opción válida.")