from Main.mysql_connection import select
from typing import Optional, Dict, Any

def obtenerHabitacionPorReservaId(reserva_id: int) -> Optional[Dict[str, Any]]:
    rows = select(
       "SELECT h.id, h.capacidad, h.tarifa, h.estado, h.fecha_habitacion_habilitada "
       "FROM Habitacion AS h "
       "JOIN Reserva r ON h.id = r.habitacion_id "
       "WHERE r.id = %s " 
       "LIMIT 1",
       (reserva_id,)
    )
    
    if not rows:
        return None
    
    id_, capacidad, tarifa, estado, fecha_habilitada = rows[0]
    return {
        "id": id_,
        "capacidad": capacidad,
        "tarifa": tarifa,
        "estado": estado,
        "fecha_habitacion_habilitada": fecha_habilitada
    }