from shared.mysql_connection import select

def validacionAdmin(user_id: int) -> bool:
    rol = select(
        "SELECT tipo FROM persona WHERE id = %s", (user_id,)
    )
    if rol and rol[0][0] == 'administracion':
        return True
    return False