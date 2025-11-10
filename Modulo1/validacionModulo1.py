from __future__ import annotations
from datetime import datetime, timedelta
from typing import Dict, Any, Tuple

_FORMATOS = (
    "%Y-%m-%d %H:%M:%S",   # 2025-11-10 14:00:00
    "%Y-%m-%d %H:%M",      # 2025-11-10 14:00
    "%Y-%m-%d",            # 2025-11-10
)


def parse_datetime(s: str) -> datetime:
    # Intentamos convertir la fecha/hora a los formatos comunes, si ninguno funciona, lanzamos error.
    s = s.strip()
    for fmt in _FORMATOS:
        try:
            # Intenta convertir els tring s a datetime usansdo ese formato.
            return datetime.strptime(s, fmt)
        # si no matchea, lanzamos valueError y seguimso con el siguiente formato.
        except ValueError:
            pass
    raise ValueError(
        f"Fecha inválida: '{s}'. Formatos válidos: " + ", ".join(_FORMATOS)
        # Si el for termino y ningún formato funcionó, levantamos nosotros un ValueError con un mensaje enumerando lso formatos validos.
    )


# ------------- Validaciones -------------
def validar_entradas(capacidad: int,
                     fecha_check_in: datetime,
                     fecha_check_out: datetime) -> Tuple[bool, Dict[str, Any]]:
    """
    Reglas:
    1) fecha_check_in < fecha_check_out
    2) número de noches <= 14 (equiv. delta <= 14 días)
    3) capacidad entre 1 y 4
    Devuelve: (es_valido, detalle_por_regla)
    """
    detalle: Dict[str, Any] = {}

    # Regla 1
    regla1_ok = fecha_check_in < fecha_check_out
    detalle["fecha_in_menor_a_out"] = {
        "ok": regla1_ok,  # Guardamos el resultado booleano.
        # Formato iso para imprimir prolijo.
        "in": fecha_check_in.isoformat(sep=" "),
        # Formato iso para imprimir prolijo.
        "out": fecha_check_out.isoformat(sep=" "),
        # Este texto solo se muestra si regla1_ok es falso
        "msg": "Fecha de entrada debe ser menor a la de salida."
    }

    # Regla 2: noches <= 14
    delta = fecha_check_out - fecha_check_in
    # Si por ejemplo
    # fecha_check_in = 2025-11-10 14:00
    # fecha_check_out = 2025-11-12 11:00
    # Delta = 1 día y 24 horas, pero delta.days=1 y delta.seconds=21*3600=75600

    regla2_ok = delta <= timedelta(days=14)
    # noches aproximadas (si hay horas/minutos, contamos una noche más)
    noches = delta.days + (1 if delta.seconds > 0 else 0)
    detalle["noches_menor_igual_14"] = {
        "ok": regla2_ok,
        "noches_calculadas": noches,
        "delta_horas": round(delta.total_seconds() / 3600, 2),
        "msg": "La cantidad de noches no puede superar 14."
    }

    # Regla 3: capacidad entre 1 y 4
    regla3_ok = (1 <= capacidad <= 4)
    detalle["capacidad_entre_1_y_4"] = {
        "ok": regla3_ok,
        "capacidad": capacidad,
        "msg": "La capacidad debe estar entre 1 y 4 huéspedes."
    }

    # Solo es valido si cumple las 3 reglas
    es_valido = regla1_ok and regla2_ok and regla3_ok
    return es_valido, detalle

# ---------- Main de prueba (solo para testear este archivo) ----------


def _pedir_int(msg: str) -> int:
    while True:
        try:
            # Eliminamos espacios y lo transformamos en entero
            return int(input(msg).strip())
        except ValueError:
            print("  → Ingrese un número entero válido.")
        # Si no es un numero, mostramos que es invalido y seguimso en loop.


def _pedir_dt(msg: str) -> datetime:
    while True:
        try:
            # Usamos la funcion para parsear a datetime.
            return parse_datetime(input(msg))
        except ValueError as e:
            print("  →", e)  # Mostramso el ValuError que nos envia parse_datetime


def _resultados_validaciones(ok: bool, detalle: Dict[str, Any]) -> None:
    # ok es el booleano global recibido de validar entradas.
    # detalle es el dict con el estado de cada regla.
    print("\n===== RESULTADO DE VALIDACIÓN =====")
    print(f"VALIDACIÓN GLOBAL: {'OK' if ok else 'FALLÓ'}\n")

    items = [
        ("fecha_in_menor_a_out", "Fecha de entrada < fecha de salida"),
        ("noches_menor_igual_14", "Número de noches ≤ 14"),
        ("capacidad_entre_1_y_4", "Capacidad entre 1 y 4"),
    ]
    for key, titulo in items:
        info = detalle.get(key, {})
        estado = "OK" if info.get("ok") else "FALLÓ"
        print(f"- {titulo}: {estado}")
        if key == "fecha_in_menor_a_out":
            print(f"    in : {info.get('in')}")
            print(f"    out: {info.get('out')}")
        if key == "noches_menor_igual_14":
            print(f"    noches calculadas: {info.get('noches_calculadas')}")
            print(f"    delta (horas)    : {info.get('delta_horas')}")
        if key == "capacidad_entre_1_y_4":
            print(f"    capacidad        : {info.get('capacidad')}")
        if not info.get("ok"):
            print(f"    mensaje          : {info.get('msg')}")
    print("===================================\n")


if __name__ == "__main__":
    print("=== TEST Validación Módulo 1 ===")
    print("Formatos de fecha aceptados:")
    print("  - YYYY-MM-DD HH:MM:SS")
    print("  - YYYY-MM-DD HH:MM")
    print("  - YYYY-MM-DD\n")

    cap = _pedir_int("Capacidad (1 a 4): ")
    f_in = _pedir_dt("Fecha de entrada: ")
    f_out = _pedir_dt("Fecha de salida : ")

    ok, det = validar_entradas(cap, f_in, f_out)
    _resultados_validaciones(ok, det)
