# MÓDULO 3: Confirmación de la Reserva

## Objetivo

Confirmar una reserva existente mediante la verificación del pago correspondiente.  
El proceso utiliza el submódulo **`realizacionDelPago`**, el cual devuelve un valor booleano que indica si el pago fue exitoso (`true`) o no (`false`).  
Según ese resultado, la reserva se actualiza en la base de datos:  
- Si el pago fue **realizado correctamente**, el estado pasa a `confirmada`.  
- Si el pago **falló**, la reserva permanece en `pendiente`.

---

## Entradas

- **reserva_id** *(número)*: Identificador único de la reserva a confirmar.

---

## Reglas y Validaciones

1. La reserva debe existir en el sistema.  
2. El estado inicial debe ser **`pendiente`**.  
3. Solo si el módulo `realizacionDelPago` devuelve `true`, se actualiza el estado a **`confirmada`**.  
4. En caso contrario, la reserva permanece **sin cambios**.  

---

## Resultado

- Estado actualizado a "confirmada" en caso de éxito, sino, no se cambia nada.  

---

## Algoritmo

1. **Ingreso de datos**  
   - Leer el `id` de la reserva.  

2. **Ejecutar módulo de pago**  
   - Llamar a `realizacionDelPago()`.  
   - Recibir un valor booleano (`TRUE` = pago exitoso / `FALSE` = pago fallido).

3. **Actualizar la reserva**  
   - Si el valor booleano es `TRUE` → actualizar `reserva.estado = "confirmada"`.  
   - Si el valor booleano es `FALSE` → mantener `reserva.estado = "pendiente"`.

4. **Escribir los cambios en la base de datos.**


---

## Refinamiento – Nivel 1

1. **Ingreso de datos**
   - Recibir `id` de reserva y datos del pago.

2. **Realización del pago**
   - Enviar los datos al módulo `realizacionDelPago`.  
   - Esperar respuesta booleana (pago realizado o no).

3. **Actualizar la reserva**
   - Buscar la reserva por id.  
   - Si no existe → mostrar error.  
   - Si existe y pago realizado = `TRUE` → actualizar estado a `"confirmada"`.  
   - Si pago realizado = `FALSE` → dejar reserva sin cambios.

4. **Escritura**
   - Guardar cambios en la base de datos.


---

## Refinamiento – Nivel 2

1. **Obtener id de reserva.**  
2. **Buscar la reserva en la base de datos.**  
   - Si no se encuentra → “Error: reserva inexistente”.  
3. **Enviar información al módulo de pago.**  
   - `pagoRealizado ← realizacionDelPago(datos_del_pago)`  
4. **Actualizar reserva:**
   - Si `pagoRealizado = TRUE`:  
     - `reserva.estado ← "confirmada"`  
     - `guardar(reserva)`  
     - Mostrar “Reserva confirmada correctamente.”  
   - Sino:  
     - Mostrar “El pago no se realizó. La reserva permanece **sin cambios**.”

---

## Pseudocódigo

```pseudo
PROCESO ConfirmarReserva(reserva_id)
    // Paso 1: Buscar la reserva
    reserva ← BUSCAR_RESERVA(reserva_id)
    SI reserva = NULO ENTONCES
        MOSTRAR "Error: reserva inexistente"
        TERMINAR
    FIN SI

    // Paso 2: Llamar al módulo de pago
    pagoExitoso ← realizacionDelPago()

    // Paso 3: Actualizar la reserva según el resultado
    SI pagoExitoso = VERDADERO ENTONCES
        reserva.estado ← "confirmada"
        GUARDAR_RESERVA(reserva)
        MOSTRAR "Reserva confirmada correctamente."
    SINO
        MOSTRAR "El pago no fue realizado.."
    FIN SI
FIN PROCESO
