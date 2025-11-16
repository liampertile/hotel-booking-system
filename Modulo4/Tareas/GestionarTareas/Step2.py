from Modulo4.Tareas.ValidacionDeInputs.ValidacionIniciarTarea import validacionIniciarTarea
from Modulo4.Tareas.ValidacionDeInputs.ValidacionFinalizarTarea import validacionFinalizarTarea
from Modulo4.Tareas.ValidacionDeInputs.ValidacionValidarTarea import validacionValidarTarea
from Modulo4.Tareas.GestionarTareas.IniciarTarea import iniciarTarea
from Modulo4.Tareas.GestionarTareas.FinalizarTarea import finalizarTarea
from Modulo4.Tareas.GestionarTareas.ValidarTarea import validarTarea

def step2(tarea_id: str, admin_id: int):
    try:
        while True:
            print(f"\n|---------| GESTIÓN DE TAREA {tarea_id} |---------|\n")
            print(" Ingrese el número de opción según corresponda:")
            print(" 1. Iniciar tarea")
            print(" 2. Finalizar tarea")
            print(" 3. Validar tarea finalizada")
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
                    case '3':
                        avanzar = validacionValidarTarea(tarea_id, admin_id)
                        if avanzar:
                            while True:
                                validada = ''
                                print("\n¿Cómo encontró la tarea finalizada?")
                                print(" 1. Bien realizada")
                                print(" 2. Mal realizada")
                                print("Ingrese 'q' en caso de cancelar la operación.\n")
                                print("|---------------------------------------------|\n\n")
                                estado = input("Ingrese la opción ( 1 - 2 ): ")
                                if estado == '1':
                                    validada = 'bienHecha'
                                elif estado == '2':
                                    validada = 'malHecha'
                                elif estado.lower() == 'q':
                                    return
                                else:
                                    print("Ingrese una opción válida.")
                                    continue
                                hecho = validarTarea(tarea_id, validada, admin_id)
                                if hecho:
                                    print("Tarea validada correctamente.")
                                    return
                                else:
                                    print("No se pudo validar la tarea.")
                    case _:
                        print("Opción inválida. Por favor, ingrese una opción válida.")
    except KeyboardInterrupt:
        print("\nGestión de tarea interrumpida por el usuario.")