import sys
import os

# Agrega la carpeta raíz del proyecto al path
ruta_raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz_proyecto not in sys.path:
    sys.path.append(ruta_raiz_proyecto)

from datetime import datetime
from typing import List, Tuple, Dict, Any

from shared.mysql_connection import select
from validacionModulo1 import validar_capacidad, validar_fechas  # <-- NUEVO

# ---------------- OBTENER HABITACIONES ACTIVAS ----------------#
def obtener_habitaciones_activas() -> List[Tuple[int, int, str]]:
    query = """
        SELECT h.id, h.capacidad, h.estado
        FROM Habitacion h
        WHERE h.estado <> 'inactiva'
    """
    return select(query)

# ---------------- OBTENER LISTA DE RESERVAS ----------------#
def listar_reservas(habitacion_id: int, estados: Tuple[str, ...]) -> List[Tuple[datetime, datetime]]:
    placeholders = ",".join(["%s"] * len(estados))
    query = f"""
        SELECT r.fecha_check_in, r.fecha_check_out
        FROM Reserva r
        WHERE r.habitacion_id = %s
            AND r.estado IN ({placeholders})
        ORDER BY r.fecha_check_in
    """
    params = (habitacion_id, *estados)
    return select(query, params)

# ---------------- CONSULTAR DISPONIBILIDAD ----------------#
def consultar_disponibilidad(capacidad: int,
                             fecha_check_in: datetime,
                             fecha_check_out: datetime) -> List[Dict[str, any]]:

    # ---------- VALIDACIONES ANTES DE PROCESAR ---------- #
    if not validar_capacidad(capacidad):
        return None  # error

    if not validar_fechas(fecha_check_in, fecha_check_out):
        return None  # error

    # ---------- OBTENCIÓN Y FILTRADO ---------- #
    habitaciones = obtener_habitaciones_activas()
    if not habitaciones:
        return []

    disponibles: List[Dict[str, Any]] = []

    for (hab_id, hab_capacidad, hab_estado) in habitaciones:
        if hab_capacidad < capacidad:
            continue

        reservas_activas = listar_reservas(
            habitacion_id=hab_id,
            estados=("confirmada", "pendiente"),
        )

        solapa = False
        for r_in, r_out in reservas_activas:
            if (r_in < fecha_check_out) and (r_out > fecha_check_in):
                solapa = True
                break

        if not solapa:
            disponibles.append({
                "id": hab_id,
                "capacidad": hab_capacidad,
                "estado": hab_estado,
            })

    return disponibles


# ---------------- TEST MANUAL ----------------#
if __name__ == "__main__":
    cap = 2
    f_in = datetime.fromisoformat("2024-11-10 10:00:00")
    f_out = datetime.fromisoformat("2024-11-11 10:00:00")

    libres = consultar_disponibilidad(cap, f_in, f_out)
    for h in libres:
        print(h)
