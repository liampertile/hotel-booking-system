import sys
from shared.validarExisteReservaPorId import validarExisteReservaPorId
from Modulo4.ComprobarHabitacion.ComprobarHabitacion import comprobarHabitacion
from Modulo4.Tareas.GestionarTareas.CrearTareas import crearTareas
from Modulo4.Tareas.GestionarTareas.AsignarTareas import asignarTareas
from Modulo4.Tareas.GestionarTareas.Step1 import step1
from Modulo4.Tareas.ValidacionDeInputs.ValidacionCrearTareas import validacionCrearTareas
from Modulo4.ValidacionDeLaHabitacion.VerificarValidacion import verificarValidacion
from Modulo4.Tareas.ValidacionDeInputs.ValidacionTareasCreadasPendientes import validacionTareasCreadasPendientes

def prepararHabitacion(reserva_id: int, admin_id: int):
    habitacionComprobada: bool = False
    tareasCreadas: bool = False
    tareasAsignadas: bool = False
    try:
        while True:
            print(f"\n|---------| PREPARAR HABITACIÓN PARA RESERVA {reserva_id} |---------|\n")
            print("1. Comprobar habitación")
            print("2. Crear tareas")
            print("3. Asignar tareas")
            print("4. Gestionar tareas")
            print("5. Verificar validación")
            print("0. Salir\n")
            print("|-------------------------------------------------------|\n\n")
            
            opcion = input("Opción: ")
            
            if opcion == '0':
                print("Saliendo del proceso de preparar habitación.")
                return
            else:
                ok = validarExisteReservaPorId(reserva_id)
                if not ok:
                    print("No se puede continuar sin una reserva válida.")
                    return
                else:
                    match opcion:
                        case '1':
                            habitacionComprobada = comprobarHabitacion(reserva_id)
                            if habitacionComprobada:
                                print("La habitación fue comprobada correctamente, se deben crear las tareas.")
                            else:
                                print("La habitación no puede ser preparada.")
                        case '2':
                            if not habitacionComprobada:
                                print("Primero debe comprobar la habitación antes de crear las tareas.")
                                continue
                            else:
                                tareasValidadas = validacionCrearTareas(reserva_id)
                                if not tareasValidadas:
                                    print("No se pueden crear nuevas tareas para esta reserva hasta que no se finalicen o validen las tareas existentes.")
                                else:
                                    tareasCreadas = crearTareas(reserva_id)
                                    if tareasCreadas:
                                        print(f"Tareas creadas exitosamente para la reserva {reserva_id}")
                                    else:
                                        print("No se pudieron crear las tareas.")
                        case '3':
                            tareasCreadas = validacionTareasCreadasPendientes(reserva_id)
                            if not tareasCreadas:
                                print("Primero debe crear las tareas antes de asignarlas.")
                                continue
                            else:
                                tareasAsignadas = asignarTareas(reserva_id)
                                if tareasAsignadas:
                                    print("Tareas asignadas correctamente.")
                                else:
                                    print("No se pudieron asignar las tareas.")
                        case '4':
                                step1(reserva_id, admin_id)
                        case '5':
                            hecho = verificarValidacion(reserva_id)
                            if hecho:
                                print("Verificación de validación completada correctamente.")
                            else:
                                print("No se pudo completar la verificación de validación.")
                        case _:
                            print("Ingrese una opción válida.")
    except Exception as e:
        print(f"Error en prepararHabitacion: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: py -m Modulo4.modulo4 <reserva_id> <admin_id>")
        sys.exit(1)
    try:
        reserva_id = int(sys.argv[1])
        admin_id = int(sys.argv[2])
    except ValueError:
        print("reserva_id y admin_id deben ser enteros")
        sys.exit(1)
    prepararHabitacion(reserva_id, admin_id)