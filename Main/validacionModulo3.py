from shared.mysql_connection import select

def validar_reserva(reserva_id):
    """
    verifica que:
      1. el id sea válido (numérico y positivo)
      2. la reserva exista
      3. su estado sea 'pendiente'
    retorna true si pasa todas las validaciones, false si alguna falla.
    """
    # 1. validar si es entero y 
    if not isinstance(reserva_id, int) or reserva_id <= 0: #aca me pone en duda si puede llegar a ser 0 un id, tecnicamente creo que si
        print("error: el id de reserva debe ser un número positivo.")
        return False

    # 2. validar existencia y estado
    try:
        reserva = select("SELECT estado FROM reserva WHERE id = %s", (reserva_id,))

        if not reserva:
            print("error: la reserva no existe.")
            return False

        estado_actual = reserva[0][0]   
        if estado_actual.lower() != "pendiente":             
            print(f"la reserva {reserva_id} no está pendiente (estado actual: {estado_actual}).")
            return False

        return True

    except Exception as err:
        print("error al validar la reserva:", err) #idem con lo visto en modulo 3, puede ser que aca no sea tan seguro mostrar el error como tal.
        return False
