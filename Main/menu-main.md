# MÓDULO PRINCIPAL: MAIN (con menú y validaciones previas)

## Objetivo
Orquestar la ejecución de los módulos del sistema hotelero mediante un menú, garantizando las precondiciones de negocio antes de invocar cada módulo.  
Se valida el estado y los datos requeridos en un “gateway” previo por opción.

---

## Entradas
- Fechas y cantidad de huéspedes  
- Datos personales del huésped  
- id de la habitación seleccionada  
- id de la reserva

---

## Reglas y Validaciones
1. Cada opción del menú solo se ejecuta si pasan sus precondiciones (validaciones previas).  
2. El menú se muestra en bucle hasta seleccionar “Salir”.  
3. Los módulos no se invocan si fallan sus precondiciones; se informa el motivo y se retorna al menú.  
4. Los cambios de estado respetan la secuencia operativa del negocio:  
   - Disponibilidad → Registro → Confirmación → Preparación → Check-in → Check-out.

---

## Resultado
- Operación ejecutada solo si las precondiciones se cumplen.  
- Datos y estados consistentes en la base.  

---

## Matriz de Precondiciones por Módulo

| Opción | Módulo | Precondiciones (todas deben cumplirse) |
|---|---|---|
| 1 | Consulta de disponibilidad | `fecha_in < fecha_out`, noches ≤ 14, 1 ≤ capacidad ≤ 4 |
| 2 | Registro de reserva | Huésped válido (o creable), habitación existente, capacidad suficiente, sin solapamientos en el rango |
| 3 | Confirmación de reserva | Reserva existe y está `pendiente`, datos de pago presentes; el submódulo `realizacionDelPago` decide el resultado |
| 4 | Preparación de habitación | Reserva `confirmada`, habitación no ocupada, tareas reiniciadas/asignables, personal disponible |
| 5 | Check-in | Reserva `confirmada`, habitación `preparada`, fecha actual ≥ `fecha_check_in` |
| 6 | Check-out | Reserva `confirmada`, habitación `ocupada` |

---

## Algoritmo General
1. Mostrar menú.  
2. Leer opción.  
3. Ejecutar Validaciones Previas de la opción elegida.  
4. Si validaciones OK → invocar módulo correspondiente.  
5. Si validaciones fallan → informar y volver al menú.  
6. Repetir hasta “Salir”.

---

## Refinamiento – Nivel 1 (flujos por opción)

1. **Consulta de disponibilidad**  
   - Validar fechas y capacidad.  
   - Si válido → consultar y mostrar habitaciones.  

2. **Registro de reserva**  
   - Validar: habitación existe y disponible; capacidad OK; huésped válido/creable.  
   - Si válido → crear reserva `pendiente`.  

3. **Confirmación de reserva**  
   - Validar: reserva `pendiente`.  
   - Ejecutar `realizacionDelPago`.  
   - Si `TRUE` → actualizar a `confirmada`; si `FALSE` → permanece `pendiente`.  

4. **Preparación de habitación**  
   - Validar: reserva `confirmada`, habitación no ocupada.  
   - Reiniciar tareas, asignar personal, ejecutar flujo de tareas y marcar `preparada`.  

5. **Check-in**  
   - Validar: reserva `confirmada`, habitación `preparada`, fecha actual ≥ `fecha_check_in`.  
   - Actualizar habitación → `ocupada`.  

6. **Check-out**  
   - Validar: reserva `confirmada`, habitación `ocupada`.  
   - Habitación → `libre`; reserva → `finalizada`; invocar preparación.

---

## Refinamiento – Nivel 2

PROCESO main
opcion ← -1
MIENTRAS opcion ≠ 0 HACER
MOSTRAR_MENU()
LEER opcion
    SEGÚN opcion HACER

        CASO 1:  // Consulta de disponibilidad
            fechas, capacidad ← INPUT_CONSULTA()
            SI NO VALIDAR_CONSULTA(fechas, capacidad) ENTONCES
                IMPRIMIR "Entradas inválidas para disponibilidad."
                CONTINUAR
            FIN SI
            CONSULTA_DISPONIBILIDAD(fechas, capacidad)
            CONTINUAR

        CASO 2:  // Registro de reserva
            habitacion_id, datos_huesped, fechas ← INPUT_REGISTRO()
            SI NO VALIDAR_REGISTRO(habitacion_id, datos_huesped, fechas) ENTONCES
                IMPRIMIR "Precondiciones de registro no satisfechas."
                CONTINUAR
            FIN SI
            REGISTRAR_RESERVA(habitacion_id, datos_huesped, fechas)
            CONTINUAR

        CASO 3:  // Confirmación de reserva
            reserva_id, datos_pago ← INPUT_CONFIRMACION()
            SI NO VALIDAR_CONFIRMACION(reserva_id, datos_pago) ENTONCES
                IMPRIMIR "La reserva no está en estado 'pendiente' o faltan datos de pago."
                CONTINUAR
            FIN SI
            CONFIRMAR_RESERVA(reserva_id, datos_pago)  // invoca realizacionDelPago
            CONTINUAR

        CASO 4:  // Preparación de habitación
            reserva_id ← INPUT_PREPARACION()
            SI NO VALIDAR_PREPARACION(reserva_id) ENTONCES
                IMPRIMIR "Reserva no confirmada, habitación ocupada o personal insuficiente."
                CONTINUAR
            FIN SI
            PREPARAR_HABITACION(reserva_id)
            CONTINUAR

        CASO 5:  // Check-in
            reserva_id, identificacion ← INPUT_CHECKIN()
            SI NO VALIDAR_CHECKIN(reserva_id, identificacion) ENTONCES
                IMPRIMIR "Precondiciones de check-in no satisfechas."
                CONTINUAR
            FIN SI
            CHECK_IN(reserva_id, identificacion)
            CONTINUAR

        CASO 6:  // Check-out
            reserva_id ← INPUT_CHECKOUT()
            SI NO VALIDAR_CHECKOUT(reserva_id) ENTONCES
                IMPRIMIR "Precondiciones de check-out no satisfechas."
                CONTINUAR
            FIN SI
            CHECK_OUT(reserva_id)
            CONTINUAR

        CASO 0:
            IMPRIMIR "Saliendo del sistema..."
        DE OTRO MODO:
            IMPRIMIR "Opción inválida."
    FIN SEGÚN
FIN MIENTRAS
FIN PROCESO


## validaciones

FUNCIÓN VALIDAR_CONSULTA(fechas, capacidad) → booleano
RETORNAR fechas.in < fechas.out
Y DIFF_DIAS(fechas) ≤ 14
Y (1 ≤ capacidad ≤ 4)

FUNCIÓN VALIDAR_REGISTRO(habitacion_id, datos_huesped, fechas) → booleano
RETORNAR HABITACION_EXISTE(habitacion_id)
Y CAPACIDAD_OK(habitacion_id, datos_huesped.cantidad)
Y SIN_SOLAPES(habitacion_id, fechas)
Y HUESPED_VALIDO_O_CREABLE(datos_huesped)

FUNCIÓN VALIDAR_CONFIRMACION(reserva_id, datos_pago) → booleano
RETORNAR RESERVA_EXISTE(reserva_id)
Y ESTADO(reserva_id) = "pendiente"
Y DATOS_PAGO_COMPLETOS(datos_pago)

FUNCIÓN VALIDAR_PREPARACION(reserva_id) → booleano
RETORNAR ESTADO(reserva_id) = "confirmada"
Y HABITACION_NO_OCUPADA(reserva_id)
Y PERSONAL_DISPONIBLE()

FUNCIÓN VALIDAR_CHECKIN(reserva_id, identificacion) → booleano
RETORNAR ESTADO(reserva_id) = "confirmada"
Y HABITACION_PREPARADA(reserva_id)
Y FECHA_ACTUAL ≥ FECHA_CHECK_IN(reserva_id)
Y IDENTIDAD_COINCIDE(reserva_id, identificacion)

FUNCIÓN VALIDAR_CHECKOUT(reserva_id) → booleano
RETORNAR ESTADO(reserva_id) = "confirmada"
Y HABITACION_OCUPADA(reserva_id)


---

## Pseudocódigo resumido de cada invocación (con validación interna defensiva)

PROCESO CONFIRMAR_RESERVA(reserva_id, datos_pago)
SI NO VALIDAR_CONFIRMACION(reserva_id, datos_pago) ENTONCES
IMPRIMIR "Precondiciones no satisfechas."
RETORNAR
FIN SI
pago_ok ← realizacionDelPago(datos_pago)
SI pago_ok ENTONCES
ACTUALIZAR_RESERVA(reserva_id, "confirmada")
IMPRIMIR "Reserva confirmada."
SINO
IMPRIMIR "Pago no realizado. Reserva permanece 'pendiente'."
FIN SI
FIN PROCESO



