import sys
import os
import random
from datetime import datetime, timedelta
import traceback

# Agrega la carpeta raíz del proyecto al path para importar módulos compartidos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shared.mysql_connection import select, commit

# ------------------ FUNCIONES AUXILIARES ------------------ #

def buscar_cliente_por_dni(dni):
    resultado = select("""
        SELECT id FROM Persona
        WHERE dni = %s AND tipo = 'cliente'
    """, (dni,))
    return resultado[0][0] if resultado else None

def crear_cliente(nombre, dni, email, telefono):
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
        print("DEBUG - Resultado de LAST_INSERT_ID():", result)

        cur.close()
        conn.close()

        return result[0] if result else None

    except Exception as e:
        print("Error al registrar la reserva:", e)
        traceback.print_exc()
        return None

# ------------------ REGISTRO EN BD ------------------ #

def registrar_reserva_db(habitacion_id, cliente_id, fecha_check_in, fecha_check_out, reserva_exitosa):
    tarifa = obtener_tarifa_habitacion(habitacion_id)
    if tarifa is None:
        print("Error: habitación no encontrada.")
        return

    cantidad_noches = (fecha_check_out - fecha_check_in).days
    if cantidad_noches <= 0:
        print("Error: el check-out debe ser posterior al check-in.")
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

# ------------------ MODO INTERACTIVO ------------------ #

def ejecutar_registro_reserva():
    reserva_exitosa_input = input("¿Desea simular una reserva en tiempo? (True/False): ").strip()
    reserva_exitosa = reserva_exitosa_input.lower() == "true"

    ids_disponibles = random.sample(range(1, 21), 5)
    print(f"IDs de habitaciones disponibles desde Módulo 1: {ids_disponibles}")
    
    try:
        habitacion_id = int(input("Seleccione el ID de habitación: "))
    except ValueError:
        print("ID inválido.")
        return

    if habitacion_id not in ids_disponibles:
        print("El ID ingresado no está en la lista de habitaciones disponibles simuladas.")
        return

    tarifa = obtener_tarifa_habitacion(habitacion_id)
    if tarifa is None:
        print("Error: la habitación no existe en la base de datos.")
        return

    fecha_check_in = datetime(2025, random.randint(1, 12), random.randint(1, 25))
    fecha_check_out = fecha_check_in + timedelta(days=random.randint(1, 5))

    print(f"Fecha de check-in simulada: {fecha_check_in.date()}")
    print(f"Fecha de check-out simulada: {fecha_check_out.date()}")

    dni = input("DNI del cliente: ")
    cliente_id = buscar_cliente_por_dni(dni)

    if not cliente_id:
        print("Cliente no encontrado, ingrese sus datos:")
        nombre = input("Nombre del cliente: ")
        email = input("Email: ")
        telefono = input("Teléfono: ")

        cliente_id = crear_cliente(nombre, dni, email, telefono)

        if not cliente_id:
            print("Error al registrar el cliente.")
            return

    registrar_reserva_db(habitacion_id, cliente_id, fecha_check_in, fecha_check_out, reserva_exitosa)

# Para pruebas manuales
if __name__ == "__main__":
    ejecutar_registro_reserva()
