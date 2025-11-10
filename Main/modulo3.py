from random import random
from shared.mysql_connection  import select, commit


def realizacion_del_pago():
    """
    simula el proceso de pago.
    tiene un 80% de probabilidad de éxito.
    """
    print("procesando pago...")
    return random() < 0.8


def confirmar_reserva(reserva_id):
    """
    confirma una reserva existente mediante la verificación del pago correspondiente.
    este módulo asume que las validaciones se hacen fuera.
    """
    try:
        #obtengo la reserva
        reserva = select("SELECT estado FROM reserva WHERE id = %s", (reserva_id,))
        if not reserva:
            print(f"error: la reserva {reserva_id} no existe.")
            return

        estado_actual = reserva[0][0] #al ser una lista de tuplas, me quedo con la primera tupla y la primer componente de la tupla, en este caso es una tupla de un componente.
        if estado_actual.lower() != "pendiente":
            print(f"la reserva {reserva_id} no está pendiente (estado actual: {estado_actual}).")
            return

        # simulamos el pago
        pago_exitoso = realizacion_del_pago()

        # actualizo campo estado dependiendo de lo arrojado anteriormente
        if pago_exitoso:
            affected = commit(
                "UPDATE reserva SET estado = 'confirmada' WHERE id = %s", #la funcion commit me devuelve las filas que afecté, entonces, si afecté filas quiere decir que cambié algo por lo tanto juego por este lado:
                (reserva_id,)
            )
            if affected > 0:
                print(f"reserva {reserva_id} confirmada correctamente.")
            else:
                print(f"no se pudo confirmar la reserva {reserva_id}.")
        else:
            print(f"el pago de la reserva {reserva_id} no fue realizado. no se realizaron cambios.")

    except Exception as err:
        print("error al confirmar la reserva:", err) #ojo, aca estoy mostrando el error, capaz no es lo mas seguro...


# if __name__ == "__main__":
#     try:
#         reserva_id = int(input("ingrese el id de la reserva: "))
#         confirmar_reserva(reserva_id)
#     except ValueError:
#         print("error: el id ingresado debe ser un número entero.")
