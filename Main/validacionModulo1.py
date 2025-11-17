from datetime import datetime

def validar_capacidad(cantidad):
    """
    Valida que la cantidad de huéspedes sea un número entero 
    positivo y no exceda la capacidad máxima (ej. 4).
    
    Nota: Asume que 'cantidad' YA es un entero (el try-except se hace en main).
    """
    if not isinstance(cantidad, int):
        # Este error es para el desarrollador, no debería pasar si se usa bien
        print("Error de desarrollo: la función de validación recibió un tipo incorrecto.")
        return False

    if cantidad <= 0:
        print("Error: la cantidad de huéspedes debe ser un número entero positivo.")
        return False
    
    # Asumo 4 como máximo, como mencionaste en tu ejemplo
    if cantidad > 4:
        print("Error: la capacidad máxima para esta consulta es de 4 huéspedes.")
        return False
    
    return True


def validar_fecha_check_in(check_in_date: datetime):
    """
    Verifica que la fecha de check-in no sea anterior a hoy.
    """
    if not isinstance(check_in_date, datetime):
         print("Error de desarrollo: la función de validación recibió un tipo incorrecto.")
         return False
         
    hoy = datetime.now().date()
    
    if check_in_date.date() < hoy:
        print("Error: La fecha de check-in no puede ser anterior a hoy.")
        return False
    
    return True


def validar_fecha_check_out(check_in_date: datetime, check_out_date: datetime):
    """
    Verifica que:
    - check-out sea estrictamente posterior a check-in
    - la estadía no supere las 14 noches
    """
    if not isinstance(check_in_date, datetime) or not isinstance(check_out_date, datetime):
         print("Error de desarrollo: la función de validación recibió un tipo incorrecto.")
         return False

    # Validación 1: Check-out debe ser DESPUÉS de Check-in
    if check_out_date <= check_in_date:
        print(f"Error: la fecha de check-out debe ser posterior al check-in ({check_in_date.strftime('%Y-%m-%d')}).")
        return False
    
    # Validación 2: Máximo de 14 noches
    duracion = (check_out_date - check_in_date).days
    if duracion > 14:
        print(f"Error: la estadía máxima es de 14 noches (ingresó {duracion} noches).")
        return False
    
    return True