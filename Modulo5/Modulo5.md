## Módulo 5: Check-in y atención al huésped

### Objetivo
Formalizar la llegada del huésped y marcar la ocupación real de la habitación. Previamente chequeando que haya una reserva confirmada, una habitacion preparada y que la fecha del check-in sea acorde a lo previsto.

---

### Entradas

- **reserva_id** *(número)*: Identificador único de la reserva para realizar el check-in.
---

### Reglas y validaciones

- El check-in debe realizarse en la fecha de check-in registrada en la reserva o en una fecha cercana (validado en el main).
- La reserva debe estar confirmada.
- Si la habitación no se encuentra preparada aún, marcar sus tareas como "mal finalizadas" para permitir el check-in igualmente.
---

### Salida

- La habitación cambia su estado a **"ocupada"**.
- Mensaje informativo con el resultado del proceso.
---

### Algoritmo

1. Verificar que la habitación asociada esté en estado **"preparada"**. 
2. Actualizar el estado de la habitación a **"ocupada"**.
3. Retornar el estado de la operación y la confirmación de la ocupación.
---

### Refinamiento - Nivel 1

1.  **Validar Habitación:**
    * 1.1. Obtener la habitación vinculada a la reserva.
    * 1.2. Verificar que el estado de la habitación sea **"preparada"**.
2.  **Registrar ocupación:**
    * 2.1. Marcar la habitación como **"Ocupada"**.
3.  **Devolver confirmación.**
---

### Refinamiento - Nivel 2


1.  **Validar Habitación**
    * 1.1. Obtener la habitación vinculada a la `reserva.habitacion_id`.
    * 1.2. Si el estado de la habitación no es **"preparada"** 
	    * 1.2.1 Para cada tarea en habitación
		    * 1.2.1.1 si tarea.estado ≠ "Finalizada"
			    * 1.2.1.1.1 marcar tarea.estado = "Mal Finalizada"
		* 1.2.2. marcar estado de habitacion = **"preparada"**
2.  **Registrar Ocupación:**
    * 2.1. Modificar el estado de la habitación a **"ocupada"**.
3.  **Salida:**
    * 3.1. MOSTRAR ”Check-in realizado. Habitación `habitacion.id` ocupada por la Reserva `reserva_id`.”
  

```pseudo
INICIO CHECK_IN(reserva_id, identificacion_huesped)

// 1. Validar Habitación
habitacion ← BUSCAR_HABITACION(reserva.habitacion_id)
SI habitacion.estado ≠ "preparada" ENTONCES
   Para cada tarea en habitación
      SI tarea.estado ≠ "finalizado" ENTONCES
         tarea.estado = "mal Finalizado"
	habitacion.estado = "preparada" 
FIN SI

// 2. Registrar Ocupación
habitacion.estado ← "ocupada"

// 3. Salida
MOSTRAR "Check-in realizado. Habitación " + habitacion.id + " ocupada."

FIN
```
