from datetime import datetime

def validar_capacidad(cantidad):
    """
    Valida que la cantidad de huéspedes ingresada sea un número entero positivo.
    """
    if not isinstance(cantidad, int) or cantidad <= 0:
        print("Error: la cantidad de huéspedes debe ser un número entero positivo.")
        return False
    return True


from datetime import datetime

def validar_fechas(check_in: datetime, check_out: datetime):
    """
    Verifica que:
    - las fechas sean datetime
    - check-in sea anterior a check-out
    - ambas fechas sean posteriores o iguales a hoy
    """
    if not isinstance(check_in, datetime) or not isinstance(check_out, datetime):
        print("Error: las fechas deben tener formato datetime.")
        return False

    # No permitir fechas hacia atrás
    hoy = datetime.now().date()
    if check_in.date() < hoy or check_out.date() < hoy:
        print("Error: las fechas no pueden ser anteriores a hoy.")
        return False

    if check_in >= check_out:
        print("Error: la fecha de check-out debe ser posterior al check-in.")
        return False

    return True