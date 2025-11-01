## Módulo 5: Check-in y atención al huésped

### Objetivo
Formalizar la llegada del huésped y marcar la ocupación real de la habitación. Este proceso debe asegurar que la reserva esté confirmada, la habitación esté preparada y se realice dentro del rango de la fecha de check-in.

---

### Entradas

- **reserva_id** *(número)*: Identificador único de la reserva para realizar el check-in.
---

### Reglas y validaciones

- El check-in debe realizarse en la fecha de check-in registrada en la reserva o en una fecha cercana (dentro de un rango de tolerancia, por ejemplo, el mismo día). ELIMINAR
---

### Salida

- La habitación cambia su estado a **"ocupada"**.
- Mensaje informativo con el resultado del proceso.
---

### Algoritmo

1. Validar la existencia de la reserva y su estado (debe ser **"confirmed"**). ELIMINAR
2. Verificar la identidad del huésped, comparando la identificación presentada con la registrada en la reserva. ELIMINAR
3. Verificar que la habitación asociada esté en estado **"preparada"**. 
4. Comprobar que la operación se realice dentro de la fecha de check-in permitida.
5. Actualizar el estado de la habitación a **"ocupada"**.
6. Retornar el estado de la operación y la confirmación de la ocupación.
---

### Refinamiento - Nivel 1

1.  **Validar reserva y habitación:**
    * 1.1. Buscar reserva que coincida con el numero de reserva del cliente.
    * 1.2. Verificar que el estado de la reserva sea **"confirmed"**.
    * 1.3. Comparar la `identificacion_huesped` presentada con el documento del titular de la reserva.
2.  **Validar Habitación:**
    * 2.1. Obtener la habitación vinculada a la reserva.
    * 2.2. Verificar que el estado de la habitación sea **"preparada"**.
3.  **Validar fecha de check-in:**
    * 3.1. Comprobar que la fecha actual sea igual o posterior a la `fecha_check_in` de la reserva.
4.  **Registrar ocupación:**
    * 4.1. Marcar la habitación como **"Ocupada"**.
5.  **Devolver confirmación.**
---

### Refinamiento - Nivel 2

1.  **Validar Reserva y Habitación:**
    * 1.1. Buscar la reserva utilizando el `reserva_id`
        * 1.1.1. Si la reserva no se encuentra → Error
    * 1.2. Si el estado de la reserva es distinto de **"confirmed"** → Error
    * 1.3. Obtener los datos del huésped titular asociado a la reserva.
        * 1.3.1. Si la `identificacion_huesped` no coincide con el documento del huésped titular → Error
2.  **Validar Habitacion**
    * 2.1. Obtener la habitación vinculada a la `reserva.habitacion_id`.
    * 2.2. Si el estado de la habitación es distinto de **"preparada"** → Error
3.  **Validar Fecha y Hora:**
    * 3.1. Si `fecha actual` < `fecha_check_in` → Error
4.  **Registrar Ocupación:**
    * 4.1. Modificar el estado de la habitación a **"ocupada"**.
5.  **Salida:**
    * 5.1. MOSTRAR ”Check-in realizado. Habitación `habitacion.id` ocupada por la Reserva `reserva_id`.”
  

```pseudo
INICIO CHECK_IN(reserva_id, identificacion_huesped)

// 1. Validar Reserva
reserva ← BUSCAR_RESERVA(reserva_id)
SI reserva = NULO ENTONCES
    MOSTRAR "Error: Reserva inexistente"
    TERMINAR
FIN SI

SI reserva.estado ≠ "confirmed" ENTONCES
    MOSTRAR "Error: La reserva no está confirmada"
    TERMINAR
FIN SI

// 2. Validar Identidad
huesped ← BUSCAR_HUESPED(reserva.huesped_id)
SI huesped.dni ≠ identificacion_huesped ENTONCES
    MOSTRAR "Error: La identificación no coincide con el titular"
    TERMINAR
FIN SI

// 3. Validar Habitación
habitacion ← BUSCAR_HABITACION(reserva.habitacion_id)
SI habitacion.estado ≠ "preparada" ENTONCES
    MOSTRAR "Error: La habitación no está lista para el check-in"
    TERMINAR
FIN SI

// 4. Validar Fecha
SI FECHA_ACTUAL < reserva.fecha_check_in ENTONCES
    MOSTRAR "Error: Check-in anticipado no permitido"
    TERMINAR
FIN SI

// 5. Registrar Ocupación
habitacion.estado ← "ocupada"

// 6. Salida
MOSTRAR "Check-in realizado. Habitación " + habitacion.id + " ocupada."

FIN
```
