import sys
import os
import random
from datetime import datetime, timedelta
import traceback

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shared.mysql_connection import select, commit

# --------------------------------------------------------------------
# VALIDACIONES DE CAMPOS
# --------------------------------------------------------------------

def validar_dni(dni: str):
    if not dni.isdigit():
        print("Error: el DNI debe contener solo números.")
        return False
    if not (7 <= len(dni) <= 8):
        print("Error: el DNI debe tener entre 7 y 8 dígitos.")
        return False
    return True

def validar_telefono(telefono: str):
    if not telefono.isdigit():
        print("Error: el teléfono debe contener solo números.")
        return False
    if not (10 <= len(telefono) <= 14):
        print("Error: el teléfono debe tener entre 10 y 14 dígitos.")
        return False
    return True

def validar_email(email: str):
    if "@" not in email or ".com" not in email:
        print("Error: el email debe contener '@' y terminar en '.com'.")
        return False
    return True

def validar_nombre(nombre: str):
    if not nombre.strip():
        print("Error: el nombre no puede estar vacío.")
        return False
    if not nombre.replace(" ", "").isalpha():
        print("Error: el nombre solo puede contener letras.")
        return False
    return True


# --------------------------------------------------------------------
# FUNCIONES AUXILIARES
# --------------------------------------------------------------------

def buscar_cliente_por_dni(dni):
    resultado = select("""
        SELECT id FROM Persona
        WHERE dni = %s AND tipo = 'cliente'
    """, (dni,))
    if resultado:
        print(f"Cliente encontrado con ID: {resultado[0][0]}")
    else:
        print("Cliente no encontrado")
    return resultado[0][0] if resultado else None


def crear_cliente(nombre, dni, email, telefono):
    """
    Ahora este método VALIDA todos los datos antes de insertar.
    """

    if not validar_nombre(nombre):
        return None
    if not validar_dni(dni):
        return None
    if not validar_email(email):
        return None
    if not validar_telefono(telefono):
        return None

    try:
        query = """
            INSERT INTO persona (nombre, dni, email, telefono, tipo)
            VALUES (%s, %s, %s, %s, %s)
        """

        affected_rows = commit(query, (nombre, dni, email, telefono, "cliente"))
        if affected_rows > 0:
            resultado = select("SELECT id FROM persona WHERE dni = %s", (dni,))
            if resultado:
                return resultado[0][0]

        return None

    except Exception as e:
        print("Error al crear cliente:", e)
        traceback.print_exc()
        return None


def obtener_tarifa_habitacion(habitacion_id):
    resultado = select("SELECT tarifa FROM Habitacion WHERE id = %s", (habitacion_id,))
    return resultado[0][0] if resultado else None


def crear_reserva(habitacion_id, cliente_id, estado, monto, fecha_check_in, fecha_check_out):
    print("DEBUG - Insertando reserva con:")
    print(f"Habitación ID: {habitacion_id}")
    print(f"Cliente ID: {cliente_id}")
    print(f"Monto: {monto}")
    print(f"Check-in: {fecha_check_in}")
    print(f"Check-out: {fecha_check_out}")

    import mysql.connector
    from dotenv import load_dotenv

    load_dotenv()

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Reserva (
                habitacion_id, cliente_id, cantidad_huespedes, estado, monto, fecha_check_in, fecha_check_out
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            habitacion_id,
            cliente_id,
            1,
            estado,
            monto,
            fecha_check_in,
            fecha_check_out
        ))
        conn.commit()

        cur.execute("SELECT LAST_INSERT_ID()")
        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0] if result else None

    except Exception as e:
        print("Error al registrar la reserva:", e)
        traceback.print_exc()
        return None


def registrar_reserva_db(habitacion_id, cliente_id, fecha_check_in, fecha_check_out, reserva_exitosa):
    tarifa = obtener_tarifa_habitacion(habitacion_id)
    if tarifa is None:
        print("Error: habitación no encontrada.")
        return

    cantidad_noches = (fecha_check_out - fecha_check_in).days
    if cantidad_noches <= 0:
        print("Error: check-out debe ser posterior al check-in.")
        return

    monto = tarifa * cantidad_noches
    estado = "pendiente" if reserva_exitosa else "cancelada"

    reserva_id = crear_reserva(
        habitacion_id,
        cliente_id,
        estado,
        monto,
        fecha_check_in,
        fecha_check_out
    )

    if reserva_id:
        print("\nReserva registrada exitosamente.")
        print(f"Número de reserva: {reserva_id}")
        print(f"Estado inicial: {estado}")
        print(f"Total calculado: ${monto:.2f} por {cantidad_noches} noche(s)")
    else:
        print("Error al registrar la reserva.")
