import sys
import os
from datetime import datetime

# Agregar la carpeta raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imports
from modulo1 import consultar_disponibilidad
from modulo2 import registrar_reserva_db, crear_cliente, buscar_cliente_por_dni
from modulo3 import confirmar_reserva
from Modulo4.modulo4 import prepararHabitacion
from Modulo5.Modulo5 import check_in
from shared.mysql_connection import select


def menu():
    while True:
        print("\n" + "=" * 40)
        print("       SISTEMA DE GESTIÓN HOTELERA")
        print("=" * 40)
        print("1. Consultar disponibilidad y registrar reserva")
        print("2. Confirmar reserva")
        print("3. Preparar habitación (Módulo 4)")
        print("4. Check-in (Módulo 5)")
        print("5. Salir")
        print("=" * 40)

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            try:
                # ---------------------------------------
                # ENTRADAS DEL USUARIO
                # ---------------------------------------
                cantidad_str = input("Ingrese la cantidad de huéspedes: ").strip()
                try:
                    cantidad = int(cantidad_str)
                except ValueError:
                    print("Error: la cantidad de huéspedes debe ser un número entero.")
                    continue

                check_in_str = input("Fecha de check-in (YYYY-MM-DD): ").strip()
                check_out_str = input("Fecha de check-out (YYYY-MM-DD): ").strip()

                try:
                    check_in = datetime.strptime(check_in_str, "%Y-%m-%d")
                    check_out = datetime.strptime(check_out_str, "%Y-%m-%d")
                except ValueError:
                    print("Error: formato de fecha incorrecto. Use YYYY-MM-DD.")
                    continue

                # ---------------------------------------
                # CONSULTAR DISPONIBILIDAD (MÓDULO 1)
                # ---------------------------------------
                disponibles = consultar_disponibilidad(cantidad, check_in, check_out)

                # 1) Error de validaciones → módulo 1 ya mostró el mensaje
                if disponibles is None:
                    continue

                # 2) No hay habitaciones
                if disponibles == []:
                    print("No hay habitaciones disponibles en ese rango.")
                    continue

                # 3) Habitaciones encontradas
                print("\nHabitaciones disponibles:")
                for hab in disponibles:
                    try:
                        id_ = hab["id"]
                        capacidad = hab["capacidad"]
                        estado = hab.get("estado", "desconocido")

                        tarifa_resultado = select(
                            "SELECT tarifa FROM Habitacion WHERE id = %s", (id_,)
                        )
                        tarifa = tarifa_resultado[0][0] if tarifa_resultado else 0.0

                        print(f"ID: {id_} | Capacidad: {capacidad} | Estado: {estado} | Tarifa: ${tarifa:.2f}")
                    except Exception as e:
                        print("Error al mostrar habitación:", e)

                # ---------------------------------------
                # CONFIRMAR SI QUIERE RESERVAR (s/n)
                # ---------------------------------------
                while True:
                    respuesta = input(
                        "\n¿Desea registrar una reserva con alguna de estas habitaciones? (s/n): "
                    ).strip().lower()

                    if respuesta in ("s", "n"):
                        break

                    print("Respuesta inválida. Ingrese solo 's' o 'n'.")

                if respuesta == "n":
                    continue

                # ---------------------------------------
                # SELECCIÓN DE HABITACIÓN
                # ---------------------------------------
                ids_disponibles = [h["id"] for h in disponibles]
                while True:
                    try:
                        habitacion_id = int(input("Ingrese el ID de la habitación a reservar: "))
                        if habitacion_id in ids_disponibles:
                            break
                        print("ID no válido. Intente nuevamente con una habitación disponible.")
                    except ValueError:
                        print("Entrada inválida. Ingrese un número entero.")

                # ---------------------------------------
                # DATOS DEL CLIENTE
                # ---------------------------------------
                dni = input("DNI del cliente: ").strip()
                cliente_id = buscar_cliente_por_dni(dni)

                if not cliente_id:
                    print("Cliente no encontrado, ingrese sus datos:")
                    nombre = input("Nombre del cliente: ")
                    email = input("Email: ")
                    telefono = input("Teléfono: ")

                    cliente_id = crear_cliente(nombre, dni, email, telefono)

                    if not cliente_id:
                        print("Error al registrar el cliente.")
                        continue

                # ---------------------------------------
                # REGISTRAR LA RESERVA (MÓDULO 2)
                # ---------------------------------------
                registrar_reserva_db(habitacion_id, cliente_id, check_in, check_out, True)

            except Exception as e:
                print("Error inesperado al consultar disponibilidad:", e)

        elif opcion == "2":
            try:
                reserva_id = int(input("Ingrese el ID de la reserva a confirmar: "))
                confirmar_reserva(reserva_id)
            except ValueError:
                print("Debe ingresar un número entero.")

        elif opcion == "3":
            try:
                reserva_id = int(input("Ingrese el ID de la reserva a preparar: "))
                admin_id = int(input("Ingrese su ID de administrador: "))
                prepararHabitacion(reserva_id, admin_id)
            except ValueError:
                print("Los IDs deben ser enteros.")
            except Exception as e:
                print("Error al preparar habitación:", e)

        elif opcion == "4":
            try:
                reserva_id = int(input("Ingrese el ID de la reserva para check-in: "))
                check_in(reserva_id)
            except ValueError:
                print("El ID de la reserva debe ser un número entero.")
            except Exception as e:
                print("Error al realizar el check-in:", e)

        elif opcion == "5":
            print("Gracias por utilizar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor seleccione entre 1 y 5.")


if __name__ == "__main__":
    menu()
