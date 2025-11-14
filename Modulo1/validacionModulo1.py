# validacionmodulo1.py (Modificado)

from __future__ import annotations
from datetime import datetime, timedelta
from typing import Dict, Any, Tuple

_FORMATOS = (
    "%Y-%m-%d %H:%M:%S",  # 2025-11-10 14:00:00
    "%Y-%m-%d %H:%M",    # 2025-11-10 14:00
    "%Y-%m-%d",          # 2025-11-10
)

# --- Funciones de Parseo (sin cambios) ---

def parse_datetime(s: str) -> datetime:
    """
    Intenta convertir el string a datetime usando los formatos definidos.
    Lanza ValueError si ninguno funciona.
    """
    s = s.strip()
    for fmt in _FORMATOS:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    raise ValueError(
        f"Fecha inválida: '{s}'. Formatos válidos: " + ", ".join(_FORMATOS)
    )

# --- Funciones de Petición y Validación (MODIFICADAS) ---

def _pedir_capacidad(msg: str) -> int:
    """
    Pide un entero y valida que esté en el rango [1, 4].
    Repite la pregunta hasta que sea válido.
    """
    while True:
        try:
            cap_str = input(msg).strip()
            cap = int(cap_str)
            # Regla 3: capacidad entre 1 y 4
            if 1 <= cap <= 4:
                return cap
            else:
                print(f"  → Error: La capacidad debe estar entre 1 y 4. Ingresó: {cap}")
        except ValueError:
            print(f"  → Error: Ingrese un número entero válido (ej: 2). Ingresó: '{cap_str}'")

def _pedir_fecha_check_in(msg: str) -> datetime:
    """
    Pide la fecha de check-in.
    Valida formato y que no sea anterior a hoy.
    """
    hoy = datetime.now().date()
    while True:
        try:
            f_in_str = input(msg)
            f_in = parse_datetime(f_in_str)
            
            # Regla 0: no en el pasado (comparando solo la fecha)
            if f_in.date() < hoy:
                print(f"  → Error: La fecha de check-in no puede ser anterior a hoy ({hoy}).")
            else:
                return f_in # Válida
        except ValueError as e:
            print(f"  → {e}") # Muestra error de parse_datetime

def _pedir_fecha_check_out(msg: str, f_in: datetime) -> datetime:
    """
    Pide la fecha de check-out.
    Valida formato, que sea posterior al check-in y que el rango no supere los 14 días.
    """
    while True:
        try:
            f_out_str = input(msg)
            f_out = parse_datetime(f_out_str)
            
            # Regla 1: fecha_check_in < fecha_check_out
            if f_out <= f_in:
                print(f"  → Error: La fecha de check-out debe ser posterior a la de check-in ({f_in.isoformat(sep=' ')}).")
                continue # Volver a pedir

            # Regla 2: noches <= 14
            delta = f_out - f_in
            if delta > timedelta(days=14):
                noches = delta.days + (1 if delta.seconds > 0 else 0)
                print(f"  → Error: La estadía no puede superar las 14 noches (calculadas: {noches}).")
                continue # Volver a pedir
            
            return f_out # Válida
        except ValueError as e:
            print(f"  → {e}") # Muestra error de parse_datetime

# --- Función Principal (NUEVA) ---

def pedir_y_validar_entradas_modulo1() -> Tuple[int, datetime, datetime]:
    """
    Función principal de este módulo.
    Pide y valida interactivamente la capacidad y las fechas.
    
    Devuelve:
        (int, datetime, datetime): (capacidad, fecha_in, fecha_out) validadas.
    """
    print("=== Configuración de Búsqueda (Módulo 1) ===")
    print("Formatos de fecha aceptados:")
    print("  - YYYY-MM-DD HH:MM:SS")
    print("  - YYYY-MM-DD HH:MM")
    print("  - YYYY-MM-DD (ej: 2025-11-20)\n")

    # 1. Pedir Capacidad (ya valida 1-4)
    cap = _pedir_capacidad("Capacidad (1 a 4): ")

    # 2. Pedir Check-in (ya valida formato y que no sea en el pasado)
    f_in = _pedir_fecha_check_in("Fecha de entrada: ")

    # 3. Pedir Check-out (ya valida formato, orden de fechas y límite de 14 días)
    f_out = _pedir_fecha_check_out(f"Fecha de salida : ", f_in)
    
    print("\n--- Entradas validadas correctamente ---")
    print(f" Capacidad: {cap}")
    print(f" Check-in:  {f_in.isoformat(sep=' ')}")
    print(f" Check-out: {f_out.isoformat(sep=' ')}")

    return cap, f_in, f_out

# --- Bloque de Prueba (if __name__ == "__main__") ---
# Este bloque ahora solo sirve para probar este archivo de forma aislada.
# La lógica principal se moverá a 'modulo1.py'

if __name__ == "__main__":
    print("=== INICIO TEST: validacionmodulo1.py ===")
    
    # Llamamos a la nueva función principal de este módulo
    cap, f_in, f_out = pedir_y_validar_entradas_modulo1()
    
    print("\n--- TEST FINALIZADO ---")
    print("Valores recibidos del test:")
    print(f" Capacidad: {cap} (Tipo: {type(cap)})")
    print(f" Check-in:  {f_in} (Tipo: {type(f_in)})")
    print(f" Check-out: {f_out} (Tipo: {type(f_out)})")