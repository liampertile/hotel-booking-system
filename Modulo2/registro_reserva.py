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

    # Cargar variables del .env
    load_dotenv()

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cur = conn.cursor()

        # Ejecutar el INSERT
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

        # Obtener el último ID insertado en esta misma conexión
        cur.execute("SELECT LAST_INSERT_ID()")
        result = cur.fetchone()
        print("DEBUG - Resultado de LAST_INSERT_ID():", result)

        cur.close()
        conn.close()

        if result:
            return result[0]
        else:
            return None

    except Exception as e:
        print("Error al registrar la reserva:", e)
        import traceback
        traceback.print_exc()
        return None


# ------------------ LÓGICA PRINCIPAL ------------------ #

def registrar_reserva(habitacion_id, cliente_id, fecha_check_in, fecha_check_out):
    tarifa = obtener_tarifa_habitacion(habitacion_id)
    if tarifa is None:
        print("Error: habitación no encontrada.")
        return

    cantidad_noches = (fecha_check_out - fecha_check_in).days
    if cantidad_noches <= 0:
        print("Error: el check-out debe ser posterior al check-in.")
        return

    monto = tarifa * cantidad_noches

    reserva_id = crear_reserva(
        habitacion_id,
        cliente_id,
        "pendiente",
        monto,
        fecha_check_in,
        fecha_check_out
    )

    if reserva_id:
        print("\nReserva registrada exitosamente.")
        print(f"Número de reserva: {reserva_id}")
        print("Estado inicial: pendiente")
        print(f"Total calculado: ${monto:.2f} por {cantidad_noches} noche(s)")
    else:
        print("Error al registrar la reserva.")

# ------------------ PROGRAMA PRINCIPAL ------------------ #

if __name__ == "__main__":
    # Simular IDs disponibles desde el Módulo 1 (como si ya vinieran filtrados)
    ids_disponibles = random.sample(range(1, 21), 5)
    print(f"IDs de habitaciones disponibles desde Módulo 1: {ids_disponibles}")
    
    try:
        habitacion_id = int(input("Seleccione el ID de habitación: "))
    except ValueError:
        print("ID inválido.")
        sys.exit()

    # Validar si el ID ingresado está en el listado simulado
    if habitacion_id not in ids_disponibles:
        print("El ID ingresado no está en la lista de habitaciones disponibles simuladas.")
        sys.exit()

    # Validar existencia real en la base de datos
    tarifa = obtener_tarifa_habitacion(habitacion_id)
    if tarifa is None:
        print("Error: la habitación no existe en la base de datos.")
        sys.exit()

    # Generar fechas aleatorias válidas
    fecha_check_in = datetime(2025, random.randint(1, 12), random.randint(1, 25))
    fecha_check_out = fecha_check_in + timedelta(days=random.randint(1, 5))

    print(f"Fecha de check-in simulada: {fecha_check_in.date()}")
    print(f"Fecha de check-out simulada: {fecha_check_out.date()}")

    # Verificar existencia del cliente por DNI
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
            sys.exit()

    # Ejecutar registro de reserva
    try:
        registrar_reserva(habitacion_id, cliente_id, fecha_check_in, fecha_check_out)
    except Exception as e:
        print("Error inesperado al registrar la reserva.")
        traceback.print_exc()
