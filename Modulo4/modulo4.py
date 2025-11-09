# import sys
import json
# from shared.obtenerHabitacionByReservaId import obtenerHabitacionPorReservaId
# from shared.obtenerReservaPorId import obtenerReservaPorId
# from Modulo4.ComprobarHabitacion.ComprobarEstado import comprobarEstado
# from Modulo4.ComprobarHabitacion.ComprobarOcupacion import comprobarOcupacion
# from Modulo4.ComprobarHabitacion.ComprobarReserva import comprobarReserva
# from Modulo4.ComprobarHabitacion.ComprobarHabitacion import comprobarHabitacion
# from Modulo4.Tareas.CrearTareas import crearTareas
# from Modulo4.Tareas.ObtenerTareasPorReservaId import obtenerTareasPorReservaId
# from Modulo4.Tareas.AsignarTareas import asignarTareas
# from Modulo4.Tareas.GestionarTareas.GestionarTareas import gestionarTareas
from Modulo4.Tareas.GestionarTareas.Step1 import step1

# def mostrarHabitacion(reserva_id):
#     habitacion = obtenerHabitacionPorReservaId(reserva_id)
#     if habitacion is None:
#         print(json.dumps({"error": "Habitacion no encontrada"}))
#     else:
#         print(habitacion["tarifa"])


# def mostrarReserva(reserva_id):
#     reserva = obtenerReservaPorId(reserva_id)
#     if reserva is None:
#         print(json.dumps({"error": "Reserva no encontrada"}))
#     else:
#         print(reserva["monto"])

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: py -m Modulo4.ComprobarHabitacion.ComprobarReserva <reserva_id>")
        sys.exit(1)
    try:
        rid = int(sys.argv[1])
    except ValueError:
        print("reserva_id debe ser entero")
        sys.exit(1)
    step1(rid)