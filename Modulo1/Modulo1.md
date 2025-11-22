## Módulo 1: Consulta de disponibilidad

### Objetivo

Determinar qué habitaciones están libres en un rango de fechas `[fecha_check_in, fecha_check_out)` sin modificar el estado del sistema ni generar bloqueos o reservas.

### Entradas

- **fecha_check_in** _(fecha)_: inclusive, es decir, ese día la habitación debe estar libre.
- **fecha_check_out** _(fecha)_: exclusivo, ya que ese día el huésped se retirará de la habitación.
- **cantidad_huespedes** _(número)_: indica el número de huéspedes que albergará la habitación.

### Reglas y validaciones

- La habitación debe estar sin reservas en el rango de fechas comprendido entre fecha_check_in y fecha_check_out.
- La capacidad de la habitación debe ser igual o mayor a la capacidad ingresada por el usuario.
- El rangfo de capacidad es de 1 a 4 personas.
- Una persona no puede hospedarse más de 14 días en el hotel.
- No mutación de estado: la consulta no crea, bloquea o actualiza reserva ni tareas. 

### Salidas

- Lista de habitaciones disponibles, con los campos mínimos: **`id`**, **`capacidad`**, **`tarifa`**.  REVISAR CON EL PROFE.
- Sin efectos laterales: no crea ni modifica reservas/bloqueos.

### Algoritmo

```text
1. Cargar universo de habitaciones activas. 
2. Filtrar habitaciones disponibles y sin solapes, cuya capacidad sea mayor o igual a la solicitada por el usuario. 
3. Construir la lista de disponibles con las habitaciones sin solapes.
4. Devolver la lista de habitaciones disponibles (sin mutaciones).
```

### Refinamiento - Nivel 1

```text
1. Cargar universo de habitaciones activas. 
2. Filtrar habitaciones disponibles y sin solapes, cuya capacidad sea mayor o igual a la solicitada por el usuario. 
    2.1 Para cada habitación: 
        2.1.1 Comprobar que la capacidad de la habitación sea mayor o igual que la  capacidad ingresada por el usuario. 
        2.1.2 Buscar reservas activas (confirmado 𝑜 pendiente) que se solapen con el rango solicitado.
        2.1.3 Si no hay solapamiento, añadir la habitación a la lista de habitaciones disponibles. 
3. Construir la lista de disponibles con las habitaciones sin solapes. 
4. Devolver la lista de habitaciones disponibles (sin mutaciones).
```

### Refinamiento - Nivel 2

```text
1. Cargar universo de habitaciones activas. 
    1.1 Si no hay ninguna habitación activa, devolver una lista vacía. 
2. Filtrar habitaciones disponibles y sin solapes, cuya capacidad sea mayor o igual a la solicitada por el usuario. 
    2.1 Para cada habitación: 
        2.1.1 Comprobar que la capacidad de la habitación sea mayor o igual que la capacidad ingresada por el usuario.
            2.1.1.1 Si la capacidad de la habitación es mayor o igual que la capacidad ingresada por el usuario, continuar.  
            2.1.1.2 En caso contrario, continuar con la siguiente habitación. 
        2.1.2 Buscar reservas activas (confirmado 𝑜 pendiente) que se solapen con el rango solicitado. 
            2.1.2.1 Para cada reserva activa en la habitación: 
            2.1.2.2 Si la fecha de fecha_check_in de la reserva es mayor o igual a la ingresada por el usuario, y la fecha de fecha_check_out es menor o igual a la ingresada por el usuario: 
                2.1.2.2.1 Establecer solapamiento como verdadero. 
                2.1.2.2.2 Continuar con la siguiente habitación. 
        2.1.3 Si no hay solapamiento, añadir la habitación a la lista de habitaciones  disponibles. 
            2.1.3.1 Si solapamiento es falso, añadir la habitación a la lista de  habitaciones disponibles. 
3. Construir la lista de disponibles con las habitaciones sin solapes. 
4. Devolver la lista de habitaciones disponibles (sin mutaciones).
```
### Pseudocódigo

```pseudo
PROCESO ConsultarDisponibilidad(capacidad, fecha_check_in, fecha_check_out)
	//PASO 1: Cargar universo de habitaciones activas.
	habitaciones <- obtenerHabitacionesActivas()
	SI habitaciones ==  NULL ENTONCES
		Devolver []
	FIN SI

	disponibles <- []

	//PASO 2 y 3: Filtrar por capacidad y solapes, armar lista de disponibles.

	PARA CADA hab EN habitaciones HACER
		SI hab.capacidad < capacidad ENTONCES
			CONTINUAR //pasar a la siguiente habitación.
		FIN SI

		reservasActivas <- listarReservas (hab.id, estados ∈ {"confirmada","pendiente"})
		solapa <- FALSO
		i <- 0
		MIENTRAS (NO solapa) Y (i < longitud(reservasActivas)) HACER
	    	r <- reservasActivas[i]
			SI (r.fecha_check_out >= fecha_check_in) Y (r.fecha_check_in <= fecha_check_out) ENTONCES
	        	solapa <- VERDADERO
	    	FIN SI
	    	i <- i + 1
		FIN MIENTRAS
		SI NO solapa ENTONCES
			(agregar(disponibles, hab)
		FIN SI
	FIN PARA


	//PASO 4: Devolver disponibles.

	DEVOLVER disponibles
FIN PROCESO
```
