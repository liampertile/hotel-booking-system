# MÓDULO PRINCIPAL: MAIN

## Objetivo

Coordinar la ejecución secuencial de los módulos que conforman el sistema de gestión hotelera, garantizando la coherencia en el flujo de datos y estados.  
El proceso abarca desde la consulta de disponibilidad hasta el check-out, integrando cada subproceso de manera ordenada y controlada.

---

## Entradas

- fechas y cantidad de huéspedes  
- datos personales del huésped  
- id de la habitación seleccionada  
- id de la reserva

---

## Reglas y Validaciones

1. El proceso se inicia con la consulta de disponibilidad, validando fechas y capacidad.  
2. El registro de la reserva solo puede realizarse si el huésped existe o se crea correctamente.  
3. La confirmación de la reserva depende del resultado del módulo de pago.  
4. La preparación de la habitación solo puede ejecutarse sobre reservas confirmadas.  
5. El check-in requiere que la habitación esté preparada y la reserva confirmada.  
6. El check-out se realiza únicamente sobre habitaciones ocupadas y reservas confirmadas.

---

## Salida

- Reserva finalizada y habitación liberada.  
- Datos actualizados en la base de datos del sistema.  
- Historial completo de los procesos ejecutados.

---

## Algoritmo General

1. Ingreso de datos del huésped y fechas de estadía.  
2. Validar las entradas:  
   - Fecha de entrada < fecha de salida.  
   - Número de noches ≤ 14.  
   - Capacidad entre 1 y 4 huéspedes.  
3. Ejecutar el Módulo 1 (Consulta de disponibilidad).  
   - Mostrar lista de habitaciones disponibles.  
4. Seleccionar habitación y obtener datos del huésped.  
5. Ejecutar el Módulo 2 (Registro de reserva).  
   - Generar id de reserva.  
6. Ejecutar el Módulo 3 (Confirmación de reserva).  
   - Llamar al submódulo `realizacionDelPago`.  
   - Actualizar estado según resultado (pendiente / confirmada).  
7. Ejecutar el Módulo 4 (Preparación de habitación).  
   - Validar estado "confirmada".  
   - Preparar y marcar habitación como "preparada".  
8. Ejecutar el Módulo 5 (Check-in y atención al huésped).  
   - Validar habitación "preparada" y reserva "confirmada".  
   - Cambiar estado a "ocupada".  
9. Ejecutar el Módulo 6 (Check-out).  
   - Validar habitación "ocupada" y reserva "confirmada".  
   - Cambiar estado a "libre".  
   - Llamar nuevamente a `PrepararHabitación()`.  
10. Fin del proceso.

---

## Refinamiento - Nivel 1

1. Validar datos de entrada del usuario.  
   1.1. Fechas válidas y capacidad adecuada.  
   1.2. Continuar solo si se cumplen las condiciones.

2. Módulo 1: Consulta de disponibilidad  
   - Entrada: fechas y cantidad de huéspedes.  
   - Salida: lista de habitaciones disponibles.

3. Módulo 2: Registro de reserva  
   - Entrada: id de habitación y datos del huésped.  
   - Si el huésped no existe → crear usuario.  
   - Salida: id de reserva generado.

4. Módulo 3: Confirmación de reserva  
   - Entrada: id de reserva.  
   - Llamar a `realizacionDelPago()`.  
   - Si pago exitoso → actualizar estado a "confirmada".

5. Módulo 4: Preparación de habitación  
   - Validar reserva en estado "confirmada".  
   - Ejecutar tareas de limpieza, reposición y validación.  
   - Salida: habitación "preparada".

6. Módulo 5: Check-in y atención al huésped  
   - Validar habitación "preparada" y reserva "confirmada".  
   - Cambiar estado de habitación a "ocupada".

7. Módulo 6: Check-out  
   - Validar habitación "ocupada" y reserva "confirmada".  
   - Cambiar habitación a "libre" y reserva a "finalizada".  
   - Invocar nuevamente a `PrepararHabitación()`.

---

## Refinamiento - Nivel 2

1. Ingreso de datos  
   - Usuario ingresa fechas y cantidad de huéspedes.

2. Consulta de disponibilidad  
   - Validar entradas.  
   - Mostrar habitaciones disponibles.

3. Registro de reserva  
   - Comprobar existencia del huésped.  
   - Crear usuario si no existe.  
   - Asociar habitación y generar reserva.

4. Confirmación de reserva  
   - Verificar estado "pendiente".  
   - Ejecutar `realizacionDelPago`.  
   - Si TRUE → actualizar estado a "confirmada".

5. Preparación de habitación  
   - Verificar estado "confirmada".  
   - Asignar personal y tareas.  
   - Marcar habitación "preparada".

6. Check-in  
   - Verificar estado de habitación = "preparada".  
   - Verificar reserva = "confirmada".  
   - Cambiar estado habitación → "ocupada".

7. Check-out  
   - Verificar estado de habitación = "ocupada".  
   - Verificar reserva = "confirmada".  
   - Actualizar habitación → "libre".  
   - Actualizar reserva → "finalizada".  
   - Llamar al módulo de preparación.

---

## Pseudocódigo

// Módulo 1: Consulta de disponibilidad
fechas, cantidad_huespedes ← LEER_DATOS()
VALIDAR_ENTRADAS(fechas, cantidad_huespedes)
habitaciones ← CONSULTAR_DISPONIBILIDAD(fechas, cantidad_huespedes)
MOSTRAR(habitaciones)

// Módulo 2: Registro de reserva
huesped ← VERIFICAR_HUESPED(dni)
SI huesped = NULL ENTONCES
    huesped ← CREAR_HUESPED(datos_huesped)
FIN SI
reserva_id ← REGISTRAR_RESERVA(habitacion_id, huesped)

// Módulo 3: Confirmación de reserva
pagoExitoso ← realizacionDelPago(datos_pago)
SI pagoExitoso = TRUE ENTONCES
    ACTUALIZAR_RESERVA(reserva_id, "confirmada")
FIN SI

// Módulo 4: Preparación de habitación
SI ESTADO_RESERVA(reserva_id) = "confirmada" ENTONCES
    PREPARAR_HABITACION(reserva_id)
FIN SI

// Módulo 5: Check-in
SI HABITACION_PREPARADA(reserva_id) Y RESERVA_CONFIRMADA(reserva_id)
    ACTUALIZAR_HABITACION(reserva_id, "ocupada")
FIN SI

// Módulo 6: Check-out
SI HABITACION_OCUPADA(reserva_id)
    ACTUALIZAR_HABITACION(reserva_id, "libre")
    ACTUALIZAR_RESERVA(reserva_id, "finalizada")
    PREPARAR_HABITACION(reserva_id)
FIN SI

