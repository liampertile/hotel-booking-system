### Módulo 6: Check-out y liberación de la habitación

#### Objetivo
En este módulo se gestiona la salida del huésped y la liberación de la habitación, dejando el espacio listo para su posterior limpieza y preparación.  
El proceso actúa sobre las entidades **Habitación** y **Reserva**, cambiando sus estados de acuerdo al flujo normal de salida: la habitación pasa de “ocupada” a “libre” y la reserva pasa a estado “finalizada”.  
Además, al completarse el check-out, se invoca el módulo de **Preparación de la habitación**, asegurando que el cuarto quede en condiciones para un nuevo huésped.

---

#### Entradas
- **habitacion_id (número):** Identificador único de la habitación sobre la que se realiza el check-out.  
- **reserva_id (número):** Identificador único de la reserva asociada al huésped que se retira.  
- **fecha_actual (Date):** Fecha y hora en la que se realiza la operación.  
- **confirmacion_staff (boolean):** Indica si el personal del hotel confirma manualmente la salida del huésped.  

---

#### Reglas y validaciones
1. La habitación debe existir y estar asociada a una reserva válida.  
2. La habitación debe encontrarse en estado **“ocupada”**.  
3. La reserva identificada por `reserva_id` debe existir.  
4. La reserva debe encontrarse en estado **“confirmada”** o **“en curso”**.  
5. El check-out puede realizarse únicamente si:
   - Se alcanzó la fecha de salida registrada en la reserva, **o**
   - El personal confirma la salida anticipada (`confirmacion_staff = true`).  
6. Al realizar el check-out:
   - Se actualiza el estado de la **habitación** a **“libre”**.  
   - Se actualiza el estado de la **reserva** a **“finalizada”**.  
   - Se registra la **fecha de check-out real**.  
   - Se ejecuta el proceso de **Preparación de la habitación**.  

---

#### Salidas
- La habitación cambia su estado a **“libre”**.  
- La reserva pasa al estado **“finalizada”**.  
- Se registra la **fecha y hora real del check-out**.  
- Se ejecuta el módulo de **Preparación de la habitación** para dejar el cuarto en condiciones.  
- Se genera un mensaje informativo con el resultado del proceso.  

---

#### Algoritmo
1. Se libera la habitación.  
2. Se finaliza la reserva.  
3. Se prepara la habitación.  

---

#### Refinamiento - Nivel 1
1. **Se libera la habitación.**  
   1.1 Actualizar estado de la habitación.  

2. **Se finaliza la reserva.**  
   2.1 Actualizar estado de la reserva.  

3. **Se prepara la habitación.**  
   3.1 Ejecutar `PrepararHabitación(habitacion_id, reserva_id)`.  

---

#### Refinamiento - Nivel 2
1. **Se libera la habitación.**  
   1.1 Obtener la habitación por id.  
   1.2 Si la habitación no existe  
   &nbsp;&nbsp;&nbsp;&nbsp;1.2.1 Mostrar “Habitación inexistente”.  
   1.3 Sino  
   &nbsp;&nbsp;&nbsp;&nbsp;1.3.1 Si el estado de la habitación es “ocupado”  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.3.1.1 Cambiar el estado de la habitación a “libre”.  
   &nbsp;&nbsp;&nbsp;&nbsp;1.3.2 Sino  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.3.2.1 Mostrar “La habitación no se encuentra ocupada”.  

2. **Se finaliza la reserva.**  
   2.1 Obtener la reserva por id.  
   2.2 Si la reserva no existe  
   &nbsp;&nbsp;&nbsp;&nbsp;2.2.1 Mostrar “Reserva inexistente”.  
   2.3 Sino  
   &nbsp;&nbsp;&nbsp;&nbsp;2.3.1 Establecer el estado de la reserva en “finalizada”.  
   &nbsp;&nbsp;&nbsp;&nbsp;2.3.2 Registrar la fecha de check-out con la fecha actual.  

3. **Se prepara la habitación.**  
   3.1 Ejecutar `PrepararHabitación(habitacion_id, reserva_id)`.  

---

#### Pseudocódigo
```plaintext
PROCESO RealizarCheckOut(habitacion_id, reserva_id):
    LiberarHabitación(habitacion_id)
    FinalizarReserva(reserva_id)
    PrepararHabitación(habitacion_id, reserva_id)
FIN PROCESO


PROCESO LiberarHabitación(habitacion_id)
    habitación <- obtenerHabitaciónPorId(habitacion_id)
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
