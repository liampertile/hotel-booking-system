
## Módulo 3: Confirmación de Reserva

## Objetivo

Confirmar una reserva existente mediante el registro de un pago válido.  
El proceso asegura que la reserva esté activa, que el importe sea correcto, que el pago quede debidamente registrado y que, si el pago fue efectivamente capturado, la reserva cambie su estado de `pendiente` a `confirmada`.

---

## Entradas

- **reserva_id (número):** Identificador único de la reserva a confirmar.  
- %% REVISAR **staff_id (número):** Identificador del empleado (tipo *staff*) responsable de la confirmación. %%

---

## Reglas y Validaciones

1. La reserva debe existir y encontrarse en estado `pendiente`.  
2. Solo pueden confirmarse reservas que no estén canceladas ni completadas.  ELIMINAR
3. El monto del pago debe ser mayor que cero.  ELIMINAR/revisar
4. El estado del pago debe ser uno de los válidos: `pagado`, `no pagado`  (MODULO QUE SIMULA EL BANCO)
5. Todo pago registrado debe incluir método, monto, moneda, estado y fecha de creación.  ELIMINAR
6. Si la reserva está en pendiente : (sino es porque esta cancelada)
   7. Si el pago fue realizado, la reserva cambia automáticamente a estado `confirmada`.  
   8. Si el pago no fue capturado, volver al 6.

---

## Salida

- Estado final de la reserva (`confirmada` si el pago fue realizado; `cancelada` si se termino el tiempo de espera).  
---

## Algoritmo

1. Validar la existencia de la reserva y su estado actual.  
2. Verificar que el importe del pago sea mayor a 0.  
3. Registrar el pago con su monto, moneda, método y estado.  
4. Analizar el resultado del pago:  
   - Si el pago está en estado `capturado`, actualizar la reserva a `confirmada` y registrar fecha y staff responsable.  
   - En caso contrario, mantener la reserva `pendiente`.  
5. Retornar el estado final de la reserva junto con el registro del pago.

---

## Refinamiento – Nivel 1

1. **Validar datos de entrada:**
   - Verificar que la reserva exista.  
   - Validar que el estado actual sea `pendiente`.  
   - Comprobar que el monto sea mayor a 0.

2. **Registrar el pago:**
   - Crear un nuevo pago asociado a la reserva.  
   - Registrar método, moneda, monto, estado y fecha de creación.  
   - Aceptar únicamente estados válidos: `autorizado`, `capturado`, `anulado`.

3. **Confirmar la reserva (si corresponde):**
   - Si el pago fue `capturado`, actualizar estado de reserva a `confirmada`.  
   - Registrar fecha y usuario (`staff_id`) que realizó la confirmación.

---

## Refinamiento – Nivel 2

1. **Validar datos:**
   - Si la reserva no existe → Error: “Reserva inexistente”.  
   - Si la reserva no está en estado `pendiente` → Error: “Reserva no disponible para confirmar”.  
   - Si el monto ≤ 0 → Error: “Monto inválido”.

2. **Registrar pago:**
   - Crear registro de pago con los datos ingresados.  
   - Validar que el estado del pago esté dentro de los valores permitidos.  
   - Guardar fecha y hora del registro.

3. **Confirmar reserva:**
   - Si el estado del pago es `capturado`, cambiar la reserva a `confirmada`.  
   - Registrar fecha y usuario (`staff_id`) que realizó la confirmación.  
   - Si no fue capturado, mantener `pendiente`.

4. **Retornar salida:**
   - Estado final de la reserva.  
   - Datos del pago asociado.  
   - Mensaje de confirmación o aviso de pendiente.

## Pseudocódigo

```pseudo
INICIO CONFIRMAR_RESERVA

LEER reserva_id, monto, moneda, metodo_pago, estado_pago, staff_id

// Validar reserva
SI RESERVA_NO_EXISTE(reserva_id) ENTONCES
    MOSTRAR "Error: reserva inexistente"
    TERMINAR
FIN SI

SI ESTADO(reserva_id) != "pendiente" ENTONCES
    MOSTRAR "Error: la reserva no puede ser confirmada"
    TERMINAR
FIN SI

SI monto <= 0 ENTONCES
    MOSTRAR "Error: monto inválido"
    TERMINAR
FIN SI

// Registrar pago
pago := CREAR_PAGO(reserva_id, monto, moneda, metodo_pago, estado_pago, FECHA_ACTUAL)

// Confirmar reserva si el pago fue capturado
SI estado_pago = "capturado" ENTONCES
    ACTUALIZAR_ESTADO_RESERVA(reserva_id, "confirmada")
    REGISTRAR_CONFIRMACION(reserva_id, staff_id, FECHA_ACTUAL)
    MOSTRAR "Reserva confirmada correctamente"
SINO
    MOSTRAR "Reserva permanece pendiente"
FIN SI

FIN

