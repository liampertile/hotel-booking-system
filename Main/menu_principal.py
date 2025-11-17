import sys
import os
from datetime import datetime

# Agregar la carpeta raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imports
# --- IMPORT MODIFICADO ---
# from Main.validacionModulo1 import validar_capacidad, validar_fechas (Línea original)
from Main.validacionModulo1 import validar_capacidad, validar_fecha_check_in, validar_fecha_check_out
# --- FIN IMPORT MODIFICADO ---
from Main.modulo1 import consultar_disponibilidad
from Main.modulo2 import registrar_reserva_db, crear_cliente, buscar_cliente_por_dni
from Main.modulo3 import confirmar_reserva
from Main.ValidacionAdmin import validacionAdmin
from Main.listarReservas import listarReservas
from Modulo4.modulo4 import prepararHabitacion
from Modulo5.Modulo5 import check_in
from Modulo5.validacionModulo5 import validar_checkin 
from shared.mysql_connection import select
from Modulo6.modulo6 import check_out
from Modulo6.validacionModulo6 import validar_checkout

def menu():
    adminId = input("Ingrese su ID de administrador: ")
    esAdmin = validacionAdmin(int(adminId))
    if not esAdmin:
        print("Acceso denegado. Solo administradores pueden acceder al sistema.")
        return
    else:
        print("Acceso concedido. Bienvenido, administrador.")
        while True:
            print("\n" + "=" * 40)
            print("      SISTEMA DE GESTIÓN HOTELERA")
            print("=" * 40)
            print("1. Consultar disponibilidad y registrar reserva")
            print("2. Confirmar reserva")
            print("3. Preparar habitación (Módulo 4)")
            print("4. Check-in (Módulo 5)")
            print("5. Check-out (Módulo 6)")  # <-- NUEVO
            print("6. Listar reservas actuales")
            print("7. Salir")

            print("=" * 40)

            opcion = input("Seleccione una opción (1-7): ")

            if opcion == "1":
                try:
                    # ---------------------------------------
                    # --- BLOQUE DE ENTRADAS MODIFICADO ---
                    # (Usando el método de banderas)
                    # ---------------------------------------
                    
                    # --- 1. Validación de Cantidad ---
                    cantidad_valida = False
                    cantidad = 0 # Inicializamos la variable
                    while not cantidad_valida:
                        cantidad_str = input("Ingrese la cantidad de huéspedes (1-4): ").strip()
                        try:
                            cantidad = int(cantidad_str)
                            # Llamamos a la validación lógica
                            if validar_capacidad(cantidad):
                                cantidad_valida = True # ¡Éxito! Salimos del bucle
                            # Si validar_capacidad da False, imprime su propio error y el bucle repite
                        except ValueError:
                            print("Error: debe ingresar un número entero.")
                    
                    # --- 2. Validación de Check-in ---
                    check_in_valido = False
                    check_in_date = None # Inicializamos la variable
                    while not check_in_valido:
                        check_in_str = input("Fecha de check-in (YYYY-MM-DD): ").strip()
                        try:
                            check_in_date = datetime.strptime(check_in_str, "%Y-%m-%d")
                            # Llamamos a la validación lógica
                            if validar_fecha_check_in(check_in_date):
                                check_in_valido = True # ¡Éxito!
                            # Si da False, imprime su propio error y el bucle repite
                        except ValueError:
                            print("Error: formato de fecha incorrecto. Use YYYY-MM-DD.")
                    
                    # --- 3. Validación de Check-out ---
                    check_out_valido = False
                    check_out_date = None # Inicializamos la variable
                    while not check_out_valido:
                        check_out_str = input("Fecha de check-out (YYYY-MM-DD): ").strip()
                        try:
                            check_out_date = datetime.strptime(check_out_str, "%Y-%m-%d")
                            # Llamamos a la validación lógica (que depende de check_in)
                            if validar_fecha_check_out(check_in_date, check_out_date):
                                check_out_valido = True # ¡Éxito!
                            # Si da False, imprime su propio error y el bucle repite
                        except ValueError:
                            print("Error: formato de fecha incorrecto. Use YYYY-MM-DD.")

                    # --- FIN DEL BLOQUE MODIFICADO ---
                    # ---------------------------------------

                    # ---------------------------------------
                    # CONSULTAR DISPONIBILIDAD (MÓDULO 1)
                    # (Esta parte NO se toca)
                    # ---------------------------------------
                    disponibles = consultar_disponibilidad(cantidad, check_in_date, check_out_date)

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
                    # (Esta parte NO se toca)
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
                    # (Esta parte NO se toca)
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
                    # (Esta parte NO se toca)
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
                    # (Esta parte NO se toca)
                    # ---------------------------------------
                    registrar_reserva_db(habitacion_id, cliente_id, check_in_date, check_out_date, True)

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
                    
                    prepararHabitacion(reserva_id, adminId)
                except ValueError:
                    print("Los IDs deben ser enteros.")
                except Exception as e:
                    print("Error al preparar habitación:", e)

            elif opcion == "4":
                try:
                    reserva_id = int(input("Ingrese el ID de la reserva para check-in: "))

                    # 2. Ejecutamos la validación primero
                    if validar_checkin(reserva_id):
                        # 3. Si pasa, llamamos al Módulo 5 con la nueva firma
                        print("--- Iniciando Módulo 5: Check-in ---")
                        check_in(reserva_id, adminId)
                        print("--- Módulo 5: Check-in finalizado ---")
                    else:
                        # La validación ya imprimió el error específico
                        print("Operación cancelada. Volviendo al menú.")

                except ValueError:
                    print("El ID de la reserva y el ID de admin deben ser números enteros.")
                except Exception as e:
                    print(f"Error al realizar el check-in: {e}")
                    
            elif opcion == "5":
                try:
                    reserva_id = int(input("Ingrese el ID de la reserva para check-out: "))

                    
                    # Validación de precondiciones
                    # if validar_checkout(reserva_id):
                    print("--- Iniciando Módulo 6: Check-out ---")
                    check_out(reserva_id, adminId)
                    print("--- Módulo 6: Check-out finalizado ---")
                    # else:
                        # print("Precondiciones no satisfechas. Operación cancelada.")

                except ValueError:
                    print("El ID de la reserva debe ser un número entero.")
                except Exception as e:
                    print(f"Error al realizar el check-out: {e}")


            elif opcion == "6":
                listarReservas()
            
            elif opcion == "7":
                print("Gracias por utilizar el sistema. ¡Hasta luego!")
                break

            else:
                print("Opción inválida. Por favor seleccione entre 1 y 7.")


if __name__ == "__main__":
    menu()