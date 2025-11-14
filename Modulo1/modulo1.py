import sys
import os


# Esto agrega la carpeta raíz 'hotel-booking-system' al path de Python
ruta_raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz_proyecto not in sys.path:
    sys.path.append(ruta_raiz_proyecto)



# AHORA tus importaciones van después y funcionarán
from datetime import datetime
from typing import List, Tuple, Dict, Any 
from shared.mysql_connection import select 

# ... (El resto de tu código va acá abajo) ...


# Ahora tus importaciones funcionarán
# Asegúrate de que esta línea esté bien (antes tenías "import List" en vez de "from typing import...")

# ---------------- OBTENER HABITACIONES ACTIVAS ----------------#
# Devuelve tuplas (id, capacidad,estado) de habitaciones consideradas activas.


def obtener_habitaciones_activas() -> List[Tuple[int, int, str]]:
    query = """
        SELECT h.id, h.capacidad, h.estado
        FROM Habitacion h
        WHERE h.estado <> 'inactiva'
    """
    return select(query)  # Retornamos la lista de tuplas, con los elementos necesarios para identificar SOLAPE.
# ---------------- OBTENER HABITACIONES ACTIVAS ----------------#


# ---------------- OBTENER LISTA DE RESERVAS ----------------#
# Devuelve tuplas (fecha_check_in, fecha_check_out) de reservas de esa habitación, segun los estados solicitados.
# En nuestro caso serán pendientes y confirmadas.
def listar_reservas(habitacion_id: int, estados: Tuple[str, ...]) -> List[Tuple[datetime, datetime]]:
    # Tuple[str, ...] -> Es una tupla de str de longitud variable.
    placeholders = ",".join(["%s"] * len(estados))
    query = f"""
        SELECT r.fecha_check_in, r.fecha_check_out
        FROM Reserva r
        WHERE r.habitacion_id = %s
            AND r.estado IN ({placeholders})
        ORDER BY r.fecha_check_in
    """
    # No ponemos %s,%s en placeholders para no limitar el numero de strings. Lo hacemos dinámicamente.
    params = (habitacion_id, *estados)
    # *estados se usa para el desempaquetado, es decir, que cada elemento de estado se pase como parametro.
    return select(query, params)
# ---------------- OBTENER LISTA DE RESERVAS ----------------#


# ---------------- CONSULTAR DISPONIBILIDAD -----------------#
# Este proceso nos permite consultar la disponibilidad de una habitación en un rango de fechas.
# Podemos visualizar si existen o no solapamientos.
def consultar_disponibilidad(capacidad: int,
                             fecha_check_in: datetime,
                             fecha_check_out: datetime) -> List[Dict[str, any]]:

    # Obtenemos habitaciones activas.
    habitaciones = obtener_habitaciones_activas()
    if not habitaciones:
        return []

    disponibles: List[Dict[str, Any]] = []

    # Filtramos por capacidad y solapes.

    for (hab_id, hab_capacidad, hab_estado) in habitaciones:
        if hab_capacidad < capacidad:
            continue  # pasamos a la siguiente habitacion.

        reservas_activas = listar_reservas(
            habitacion_id=hab_id,
            estados=("confirmada", "pendiente"),
        )

        # Comprobamos que no haya solapamiento.
        solapa = False
        i = 0
        n = len(reservas_activas)

        while (not solapa) and (i < n):
            r_in, r_out = reservas_activas[i]

            # Solape verdadero si: r_in < fecha_out o r_out> fecha_in
            if (r_in < fecha_check_out) and (r_out > fecha_check_in):
                solapa = True
            i += 1

        if not solapa:
            disponibles.append({
                "id": hab_id,
                "capacidad": hab_capacidad,
                "estado": hab_estado,
            })

    return disponibles

# ---------------- CONSULTAR DISPONIBILIDAD -----------------#


if __name__ == "__main__":
    
    # 1. IMPORTAR LA NUEVA FUNCIÓN ÚNICA DE VALIDACIÓN
    try:
        from validacionModulo1 import pedir_y_validar_entradas_modulo1
    except ImportError as e:
        print(f"Error fatal: No se pudo importar 'validacionesModulo1.py'.")
        print(f"Asegúrate de que esté en la carpeta 'Main/'. Detalle: {e}")
        sys.exit(1) # Salimos del script


    cap, f_in, f_out = pedir_y_validar_entradas_modulo1()

    # 3. EJECUTAR LÓGICA PRINCIPAL
    print(f"\n--- Buscando habitaciones disponibles... ---")
    
    # Llamamos a tu función principal con los datos ya validados
    libres = consultar_disponibilidad(cap, f_in, f_out)
    
    # 4. Mostrar resultados
    if not libres:
        print("\nResultado: No se encontraron habitaciones disponibles para esos criterios.")
    else:
        print(f"\nResultado: ¡Se encontraron {len(libres)} habitaciones libres!")
        for h in libres:
            print(f"  - Habitación ID: {h['id']}, Capacidad: {h['capacidad']}, Estado: {h['estado']}")