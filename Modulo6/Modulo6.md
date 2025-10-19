## MÓDULO CHECK-OUT

## Objetivo
Gestionar la salida del huésped y liberar la habitación para su posterior limpieza y preparación.  
El proceso debe asegurar que la reserva esté activa, que la habitación esté actualmente ocupada y que el procedimiento se realice de manera controlada, dejando la habitación en estado **“libre”** y lista para el servicio de limpieza.

---

## Entradas

- **habitacion_id (número):** Identificador único de la habitación que se desea liberar.  
- **reserva_id (número):** Identificador único de la reserva asociada al huésped que realiza el check-out.

---

## Reglas y validaciones

1. La habitación identificada por `habitacion_id` debe existir.  
2. La reserva identificada por `reserva_id` debe existir.  
3. La habitación debe estar en estado **“ocupada”**.  
4. La reserva asociada debe estar en estado **“confirmada”** o **“en curso”**.  

Una vez realizado el check-out:

- Se actualiza el estado de la habitación a **“libre”**.  
- Se actualiza el estado de la reserva a **“finalizada”**.  
- Se ejecuta el proceso de preparación de habitación (`PrepararHabitación(habitacion_id, reserva_id)`) para dejarla lista para el próximo huésped.

---

## Salida

- La habitación queda liberada (`estado = "libre"`).  
- La reserva pasa al estado **“finalizada”**.  
- Se ejecuta el proceso de limpieza y preparación (`PrepararHabitación(habitacion_id, reserva_id)`).  
- Se muestra un mensaje informativo con el resultado del proceso y la hora exacta del check-out registrado.

---

## Descripción del módulo

Al ejecutarse el módulo, actúa sobre las tablas **Habitación** y **Reserva**.  
Cambia el estado de **"ocupado"** a **"libre"** en habitación y el estado de **Reserva** a **"finalizada"**.

---

## Algoritmo

1. Se libera la habitación.  
2. Se finaliza la reserva.  
3. Se prepara la habitación.

---

## Algoritmo – Refinamiento Nivel 1

1. Se libera la habitación.  
   - Actualizar estado de la habitación.  
2. Se finaliza la reserva.  
   - Actualizar estado de la reserva.  
3. Se prepara la habitación.  
   - Ejecutar `PrepararHabitación(habitacion_id, reserva_id)`.

---

## Algoritmo – Refinamiento Nivel 2

### Liberar habitación
1. Obtener la habitación por id.  
2. Si la habitación no existe → Mostrar **“Habitación inexistente”**.  
3. Sino, si el estado de la habitación es **“ocupado”**, cambiarlo a **“libre”**.  
4. Sino → Mostrar **“La habitación no se encuentra ocupada”**.

### Finalizar reserva
1. Obtener la reserva por id.  
2. Si la reserva no existe → Mostrar **“Reserva inexistente”**.  
3. Sino →  
   - Establecer el estado de la reserva en **“finalizada”**.  
   - Establecer la fecha de check-out con la fecha actual.

### Preparar habitación
1. Ejecutar `PrepararHabitación(habitacion_id, reserva_id)`.

---

## Pseudocódigo

```plaintext
PROCESO RealizarCheckOut(habitacion_id, reserva_id):
    LiberarHabitación(habitacion_id)
    FinalizarReserva(reserva_id)
    PrepararHabitación(habitacion_id, reserva_id)
FIN PROCESO


PROCESO LiberarHabitación(habitacion_id)
    habitación <- obtenerHabitaciónPorId(habitación_id)
    SI habitación no existe
        imprimir("Habitación inexistente")
    SINO
        SI habitación.estado == "ocupado"
            habitación.estado <- "libre"
        SINO
            imprimir("La habitación no se encuentra ocupada")
        FIN SI
    FIN SI
FIN PROCESO


PROCESO FinalizarReserva(reserva_id)
    reserva <- obtenerReservaPorId(reserva_id)
    SI reserva no existe
        imprimir("Reserva inexistente")
    SINO
        reserva.estado <- "finalizada"
        reserva.fecha_check_out <- fecha_actual
    FIN SI
FIN PROCESO
