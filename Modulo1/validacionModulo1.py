from __future__ import annotations
from datetime import datetime, timedelta
from typing import Dict, Any, Tuple

_FORMATOS = (
    "%Y-%m-%d %H:%M:%S",   # 2025-11-10 14:00:00
    "%Y-%m-%d %H:%M",      # 2025-11-10 14:00
    "%Y-%m-%d",            # 2025-11-10
)

def parse_datetime (s:str) -> datetime:
    #Intentamos convertir la fecha/hora a los formatos comunes, si ninguno funciona, lanzamos error.
    s = s.strip()
    for fmt in _FORMATOS:
        try:
            return datetime.strptime(s, fmt) #Intenta convertir els tring s a datetime usansdo ese formato.
        except ValueError: #si no matchea, lanzamos valueError y seguimso con el siguiente formato.
            pass 
    raise ValueError(
        f"Fecha inválida: '{s}'. Formatos válidos: " + ", ".join(_FORMATOS)
        #Si el for termino y ningún formato funcionó, levantamos nosotros un ValueError con un mensaje enumerando lso formatos validos.
    )


# ------------- Validaciones -------------