## Módulo 4: Preparación de la habitación

### Objetivo

En este módulo se trabaja la preparación de la habitación, previa al check-in e ingreso de un nuevo huésped. Cada actividad involucrada en dejar la habitación preparada deberá realizarse por 1 persona asignada, cumpliendo con un plazo de tiempo definido: debe ser realizada previa al horario en el que se realiza la entrada a la habitación de un nuevo huésped. Las tareas que se deben realizar para dejar la habitación preparada son `Limpiar los pisos`, `Cambiar sábanas y toallas` y `Reponer el frigobar`. Cuando cada tarea presenta `estado = "finalizado"` y se encuentra validada, la habitación puede ser habilitada para ser ocupada.

### Entradas

- **reserva_id** _(número)_: Identificador único de la reserva.

### Reglas y validaciones

- La habitación debe existir y estar asociada a una reserva válida.
- La **fecha de check-in** debe ser posterior a la fecha actual.
- La habitación **no debe estar ocupada**.
- Si la habitación ya se encuentra **en estado "preparada"**, no se vuelve a preparar.
- Todas las tareas deben reiniciarse antes de comenzar el proceso (`estado = pendiente`, `validada = noValidada`).
- Solo se pueden asignar tareas a **personal con estado "disponible"**.
- El número de personas disponibles debe ser **mayor o igual al número de tareas**.
- Cada tarea debe tener **un único responsable asignado**.
- Solo pueden iniciarse tareas en estado `"pendiente"`.
- Solo pueden finalizarse tareas en estado `"enProgreso"`.
- Solo pueden validarse tareas en estado `"finalizada"`.
- Cada tarea validada debe tener una `fecha_validación ≤ fecha_check_in`.
- La habitación se marca como **`preparada`** solo cuando todas las tareas están validadas a tiempo.
- Si alguna tarea no se valida antes del check-in, se retrasa el ingreso y se reabre la validación.

### Salidas

- Habitación con estado **`preparada`** y lista para el ingreso del nuevo huésped.

### Algoritmo

```text
1. Realizar comprobaciones de la habitación.
2. Reestablecer estado de preparación de la habitación.
3. Asignar tareas de preparación a personal disponible.
4. Gestionar ejecución de tareas.
5. Verificar que todas las tareas estén validadas para preparar la habitación.
```

### Refinamiento - Nivel 1

```text
1. Realizar comprobaciones de la habitación.
	1.1 Comprobar si la habitación asignada ya se encuentra limpia.
		1.1.1 Verificar si el estado de la habitación es "preparada"
	1.2 Comprobar si la habitación asignada ya fue reservada nuevamente.
		1.2.1 Verificar si existe una nueva reserva válida. 
	1.3 Comprobar si la habitación asignada ya no se encuentra ocupada.
		1.3.1 Verificar si el estado de la habitación asignada ya no es "ocupada".

2. Reestablecer el estado de preparación de la habitación.
	2.1 Establecer como pendiente cada actividad y el estado general de preparación de la habitación.

3. Asignar tareas de preparación a personal disponible.
	3.1. Vincular cada tarea a un personal de limpieza del hotel disponible.
	
4. Gestionar ejecución de tareas
	4.1 Iniciar tarea.
	4.2 Finalizar tarea.
	4.3 Validar tarea.

5. Verificar que todas las tareas estén validadas para preparar la habitación.
	5.1. Comprobar validez de cada tarea y verificar que la fecha de validación no sea mayor que la fecha de check-in.
```
### Refinamiento - Nivel 2

```text
1. Realizar comprobaciones de la habitación.
	1.1 Comprobar si la habitación asignada ya se encuentra limpia.
		1.1.1 Verificar si el estado de la habitación es "preparada"
			1.1.1.1 Obtener la habitación
			1.1.1.2 Si el estado es "preparada" entonces
				1.1.1.2.1 Mostrar "No se preparará la habitación porque ya se encuentra en este estado".
			1.1.1.3 Sino
				1.1.1.3.1 Mostrar "La habitación no se encuentra preparada".
	1.2 Comprobar si la habitación asignada ya fue reservada nuevamente.
		1.2.1 Verificar si existe una nueva reserva válida. 
			1.2.1.1 Obtener la reserva
			1.2.1.2 Si la fecha_check_in asociada a la reserva es mayor a la fecha_actual y las condiciones de reserva son válidas
				1.2.1.2.1 Mostrar "La habitación tiene una próxima reserva".
			1.2.1.3 Sino
				1.2.1.3.1 Mostrar "La habitación no tiene una próxima reserva".
	1.3 Comprobar si la habitación asignada ya no se encuentra ocupada.
		1.3.1 Verificar si el estado de la habitación asignada ya no es "ocupada".
			1.3.1.1 Obtener la habitación.
			1.3.1.2 Si el estado de la habitación asociada a la reserva es "ocupada"
				1.3.1.2.1 Mostrar "La habitación se encuentra ocupada, no se procede a preparar".
			1.3.1.3 Sino
				1.3.1.3.1 Mostrar "La habitación se encuentra desocupada, se procede a preparar".

2. Reestablecer el estado de preparación de la habitación.
	2.1 Establecer como pendiente cada actividad y el estado general de preparación de la habitación.
		2.1.1 Obtener la lista de tareas asociada a la habitación.
		2.1.2 Para cada tarea de la lista de tareas asociada a la habitación.
			2.1.2.1. Establecer estado en pendiente. 
			2.1.2.2. Establecer validación en FALSO.
		2.1.3 Cambiar estado de la habitación a "libre".

3. Asignar tareas de preparación a personal disponible.
	3.1. Vincular cada tarea a un personal de limpieza del hotel disponible.
		3.1.1 Obtener una lista de staff de personal de limpieza no ocupado
		3.1.2 Para tantas personas de la lista como tareas haya
			3.1.2.1 Asignar una tarea en estado “pendiente”.
       			3.1.2.2 Registrar fecha de asignación con fecha_actual.
			3.1.2.3 Registrar el staff responsable de la tarea.
        		3.1.2.4 Cambiar estado “ocupado” de la persona a FALSO.

4. Gestionar ejecución de tareas
	4.1 Iniciar tarea.
    		4.1.1 Seleccionar tarea en estado “pendiente”.
    		4.1.2 Cambiar estado a “enProgreso”.
    		4.1.3 Registrar fecha_inicio como fecha_actual.

	4.2 Finalizar tarea.
    		4.2.1 Seleccionar tarea en estado “enProgreso”.
    		4.2.2 Cambiar estado a “finalizado”.
    		4.2.3 Registrar fecha_fin como fecha_actual.

	4.3 Validar tarea.
    		4.3.1 Seleccionar tarea en estado “finalizado”.
    		4.3.2 Registrar fecha_validación como fecha_actual.
		4.3.3 Establecer el atributo validada según corresponda.

5. Verificar que todas las tareas estén validadas para preparar la habitación.
	5.1. Comprobar validez de cada tarea y verificar que la fecha de validación no sea mayor que la fecha de check-in.
		5.1.1 Obtener la lista de tareas asociadas a la habitación.
		5.1.2 Para cada tarea dentro de la lista
			5.1.2.1 Si la tarea no está validada o su fecha_validacion supera fecha_check_in
				5.1.2.1.1 Establecer que no todas las tareas están validadas
		5.1.3 Si todas las tareas están validadas
			5.1.3.1 Ejecutar EstablecerHabitacionPreparada(habitaciónId)
		5.1.4 Sino
			5.1.4.1 Regresar al menú de validación de actividades.
```
### Pseudocódigo

```pseudo
PROCESO PrepararHabitación(reserva_id):
	ComprobarHabitación(reserva_id)
    	ReestablecerEstado(reserva_id)
    	AsignarTareas(reserva_id)
    	GestionarTareas(reserva_id)
    	VerificarValidación(reserva_id)
FIN PROCESO

PROCESO ComprobarHabitación(reserva_id):
	ComprobarEstado(reserva_id)
	ComprobarReserva(reserva_id)
    	ComprobarOcupación(reserva_id)
FIN PROCESO

PROCESO ComprobarEstado(hreserva_id):
	habitacion <- obtenerHabitacionPorReservaId(reserva_id)
	SI habitacion.estado == "preparada"
		imprimir("La habitación ya se encuentra preparada, no se preparará nuevamente")
	SINO
		imprimir("La habitación no se encuentra preparada")
	FIN SI
FIN PROCESO

PROCESO ComprobarReserva(reserva_id):
	reserva <- obtenerReservaPorId(reserva_id)
	SI reserva.fecha_check_in > fecha_actual Y reserva.estado == "confirmada" ENTONCES
		imprimir("La habitación tiene una próxima reserva")
	SINO
		imprimir("La habitación no tiene una próxima reserva")
	FIN SI
FIN PROCESO

PROCESO ComprobarOcupacion(reserva_id):
	habitacion <- obtenerHabitacionPorReservaId(reserva_id)
	SI habitacion.estado == "ocupada" ENTONCES
		imprimir("La habitación se encuentra ocupada, no se procede a preparar")
	SINO
		imprimir("La habitación se encuentra desocupada, se procede a preparar")
	FIN SI
FIN PROCESO

PROCESO ReestablecerEstado(reserva_id):
	habitacion <- obtenerHabitacionPorReservaId(reserva_id)
	listaDeTareas <- habitacion.tareas
	PARA cada tarea en listaDeTareas:
		tarea.estado <- "pendiente"
		tarea.validada <- "noValidada"
	FIN PARA
	habitacion.estado <- "libre"
	habitacion.tareas <- listaDeTareas
FIN PROCESO

PROCESO AsignarTareas(reserva_id):
	habitacion <- obtenerHabitacionPorReservaId(reserva_id)
	listaDeTareas <- habitacion.tareas
	listaDePersonal <- obtenerPersonasDeLimpiezaDisponibles()
	SI longitud(listaDePersonal) < longitud(listaDeTareas) ENTONCES
		imprimir("No hay personal suficiente para realizar todas las tareas")
	SINO
		PARA i DESDE 0 HASTA minimo(longitud(listaDePersonal), longitud(listaDeTareas)):
			tarea <- listaTareas[i]
    			persona <- listaPersonal[i]
	    		tarea.estado <- "pendiente"
	    		tarea.fecha_asignacion <- fecha_actual
			tarea.staff_asignado <- persona.id
    			persona.ocupado <- VERDADERO
		FIN PARA
	FIN SI
FIN PROCESO
	
PROCESO GestionarTareas(reserva_id):
	habitacion <- obtenerHabitacionPorReservaId(reserva_id)
	IniciarTarea(habitacion.id)
    	FinalizarTarea(habitacion.id)
    	ValidarTarea(habitacion.id)
FIN PROCESO

PROCESO VerificarValidación(reserva_id)
	todasValidadas <- VERDADERO
	habitacion <- obtenerHabitacionPorReservaId(reserva_id)
	reserva <- obtenerReservaPorId(reserva_id)

	PARA cada tarea en habitación.tareas HACER
		SI tarea.validada == "noValidada" O tarea.fecha_validacion > reserva.fecha_check_in ENTONCES
            		todasValidadas <- FALSO
            		imprimir("Tarea " + tarea.id + " no validada a tiempo.")
		FIN SI
	FIN PARA
	SI todasValidadas == VERDADERO ENTONCES
		EstablecerHabitaciónPreparada(habitacion_id)
		imprimir("Habitación listra para check-in")
	SINO
		Regresar al menú de validación de actividades.
	FIN SI
FIN PROCESO

PROCESO EstablecerHabitaciónPreparada(reserva_id)
	habitacion <- obtenerHabitacionPorReservaId(reserva_id)
    	habitacion.estado <- "preparada"
    	habitacion.fecha_habitacion_habilitada <- fecha_actual
    	imprimir("Habitación lista para check-in")
FIN PROCESO

PROCESO IniciarTarea(habitacionId)
    tarea <- seleccionarTarea(habitacionId, "pending")
    SI tarea /= NULL ENTONCES
        tarea.estado <- "inProgress"
        tarea.fecha_inicio <- fecha_actual
        imprimir("Tarea " + tarea.id + " iniciada.")
    SINO
        imprimir("No hay tareas pendientes para iniciar.")
    FIN SI
FIN PROCESO

PROCESO FinalizarTarea(habitacionId)
    tarea <- seleccionarTarea(habitacionId, "inProgress")
    SI tarea ≠ NULL ENTONCES
        tarea.estado <- "finalizada"
        tarea.fecha_fin <- fecha_actual
        imprimir("Tarea " + tarea.id + " finalizada.")
    SINO
        imprimir("No hay tareas en progreso para finalizar.")
    FIN SI
FIN PROCESO

PROCESO ValidarTarea(habitacionId)
    tarea <- seleccionarTarea(habitacionId, "finished")
    SI tarea /= NULL ENTONCES
        tarea.fecha_validacion <- fecha_actual
	tarea.validada <- leer(validacion)
        imprimir("Tarea " + tarea.id + " validada correctamente.")
    SINO
        imprimir("No hay tareas finalizadas para validar.")
    FIN SI
FIN PROCESO
```
