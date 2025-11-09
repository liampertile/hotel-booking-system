from shared.mysql_connection import select

def obtenerPersonalLimpiezaLibre():
    row = select(
        "SELECT id FROM Persona WHERE ocupado = 0 and tipo = 'limpieza' LIMIT 1"
    )
    
    if not row:
        print("No hay personal de limpieza libre disponible.")
        return None
    else:
        personalId = row[0][0]
        print(f"Personal de limpieza libre encontrado: {personalId}")
        return personalId