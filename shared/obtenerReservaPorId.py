from Main.mysql_connection import select
from typing import Optional, Dict, Any

def obtenerReservaPorId(reserva_id: int) -> Optional[Dict[str, Any]]:
    rows = select(
       "SELECT id, cliente_id, habitacion_id, fecha_check_in, fecha_check_out, estado, monto, cantidad_huespedes "
       "FROM Reserva "
       "WHERE id = %s "
       "LIMIT 1",
       (reserva_id,)
    )
    
    if not rows:
        return None
    
    id_, cliente_id, habitacion_id, fecha_check_in, fecha_check_out, estado, monto, cantidad_huespedes = rows[0]
    return {
        "id": id_,
        "cliente_id": cliente_id,
        "habitacion_id": habitacion_id,
        "fecha_check_in": fecha_check_in,
        "fecha_check_out": fecha_check_out,
        "estado": estado,
        "monto": monto,
        "cantidad_huespedes": cantidad_huespedes
    }