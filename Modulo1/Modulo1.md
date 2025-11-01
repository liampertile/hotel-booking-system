## Módulo 1: Consulta de disponibilidad

### Objetivo

Determinar qué habitaciones están libres en un rango de fechas `[fecha_check_in, fecha_check_out)` sin modificar el estado del sistema ni generar bloqueos o reservas.

### Entradas

- **fecha_check_in** _(fecha)_: inclusive, es decir, ese día la habitación debe estar libre.
- **fecha_check_out** _(fecha)_: exclusivo, ya que ese día el huésped se retirará de la habitación.
- **cantidad_huespedes** _(número)_: indica el número de huéspedes que albergará la habitación.

### Reglas y validaciones

- Fechas válidas: `fecha_check_in` < `fecha_check_out` y `fecha_check_in` > `fecha_actual()`. 
- La capacidad de la habitación debe ser igual o mayor a la capacidad ingresada por el usuario.
- No mutación de estado: la consulta no crea, bloquea o actualiza reserva ni tareas. 
- Límites del rango: el máximo de noches son 14, por lo tanto, se debe validar el tamaño del intervalo. 

### Salidas

- Lista de habitaciones disponibles, con los campos mínimos: **`id`**, **`capacidad`**, **`tarifa`**.
- Sin efectos laterales: no crea ni modifica reservas/bloqueos.

### Algoritmo

```text
1. Usuario ingresa capacidad, fecha_check_in y fecha_check_out. 
2. Validar entradas: fechas, límites de noches (≤ 14) y capacidad (≥ 1 𝑦 ≤ 4). 
3. Cargar universo de habitaciones activas. 
4. Filtrar habitaciones disponibles y sin solapes, cuya capacidad sea mayor o igual a la solicitada por el usuario. 
5. Construir la lista de disponibles con las habitaciones sin solapes.
6. Devolver la lista de habitaciones disponibles (sin mutaciones).
```

### Refinamiento - Nivel 1

```text
1. Usuario ingresa capacidad, fecha_check_in y fecha_check_out. 
2. Validar entradas: fechas, límites de noches (≤ 14) y capacidad (≥ 1). 
    2.1 Validar que la fecha de fecha_check_in sea anterior a la fecha de fecha_check_out. 
    2.2 Validad que la cantidad de noches sea menor o igual a 14. 
    2.3 Validar que la capacidad sea mayor o igual a 1. 
    2.4 Validar que la capacidad sea menor o igual a 4. 
3. Cargar universo de habitaciones activas. 
4. Filtrar habitaciones disponibles y sin solapes, cuya capacidad sea mayor o igual a la solicitada por el usuario. 
    4.1 Para cada habitación: 
        4.1.1 Comprobar que la capacidad de la habitación sea mayor o igual que la  capacidad ingresada por el usuario. 
        4.1.2 Buscar reservas activas (confirmado 𝑜 pendiente) que se solapen con el rango solicitado.
        4.1.3 Si no hay solapamiento, añadir la habitación a la lista de habitaciones disponibles. 
5. Construir la lista de disponibles con las habitaciones sin solapes. 
6. Devolver la lista de habitaciones disponibles (sin mutaciones).
```

### Refinamiento - Nivel 2

```text
1. Usuario ingresa fecha de capacidad, fecha_check_in y fecha_check_out. 
    1.1 Leer la capacidad ingresada por el usuario. 
    1.2 Leer la fecha de fecha_check_in ingresada por el usuario. 
    1.3 Leer la fecha de fecha_check_out ingresada por el usuario
2. Validar entradas: fechas, límites de noches (≤ 14) y capacidad (≥ 1). 
    2.1 Validar que la fecha de fecha_check_in sea anterior a la fecha de fecha_check_out. 
        2.1.1 Si la fecha de fecha_check_in es menor a la fecha de fecha_check_out, continuar. En caso contrario arrojar error (“La fecha de fecha_check_in debe ser anterior a la fecha de fecha_check_out). 
    2.2 Validar que la cantidad de noches sea menor o igual a 14. 
        2.2.1 Calcular la diferencia de días entre la fecha de fecha_check_out y la fecha de 
    fecha_check_in. 
        2.2.2 Si la diferencia es menor o igual a 14, continuar.  
        2.2.3 En caso contrario, arrojar error (“El máximo de noches es 14”). 
    2.3 Validar que la capacidad sea mayor o igual a 1. 
        2.3.1 Si la capacidad es mayor o igual a 1, continuar.  
        2.3.2 En caso contrario, arrojar error (“El mínimo de capacidad es de 1 persona”). 
    2.4 Validar que la capacidad sea menor o igual a 4. 
        2.4.1 Si la capacidad es menor o igual a 4, continuar.  
        2.4.2 En caso contrario, arrojar error (“El máximo de capacidad es de 4 personas”). 
3. Cargar universo de habitaciones activas. 
    3.1 Si no hay ninguna habitación activa, devolver una lista vacía. 
4. Filtrar habitaciones disponibles y sin solapes, cuya capacidad sea mayor o igual a la solicitada por el usuario. 
    4.1 Para cada habitación: 
        4.1.1 Comprobar que la capacidad de la habitación sea mayor o igual que la capacidad ingresada por el usuario.
            4.1.1.1 Si la capacidad de la habitación es mayor o igual que la capacidad ingresada por el usuario, continuar.  
            4.1.1.2 En caso contrario, continuar con la siguiente habitación. 
        4.1.2 Buscar reservas activas (confirmado 𝑜 pendiente) que se solapen con el rango solicitado. 
            4.1.2.1 Para cada reserva activa en la habitación: 
            4.1.2.2 Si la fecha de fecha_check_in de la reserva es mayor o igual a la ingresada por el usuario, o la fecha de fecha_check_out es menor o igual a la ingresada por el usuario: 
                4.1.2.2.1 Establecer solapamiento como verdadero. 
                4.1.2.2.2 Continuar con la siguiente habitación. 
        4.1.3 Si no hay solapamiento, añadir la habitación a la lista de habitaciones  disponibles. 
            4.1.3.1 Si solapamiento es falso, añadir la habitación a la lista de  habitaciones disponibles. 
5. Construir la lista de disponibles con las habitaciones sin solapes. 
6. Devolver la lista de habitaciones disponibles (sin mutaciones).
```
### Pseudocódigo

```pseudo
PROCESO Modulo 1
	//PASO 1: Usuario ingresa capacidad, fecha_check_in y fecha_check_out

	LEER capacidad
	LEER fecha_check_in
	LEER fecha_check_out

	//PASO 2: Validaciones

	SI fechafecha_check_in >= fecha_check_out ENTONCES
		ArrojarError("La fecha de fecha_check_in debe ser anterior a la fecha de fecha_check_out").
		Devolver []
	FIN SI

	noches <-diffDias(fecha_check_out, fecha_check_in)
	SI noches > 14 ENTONCES
		ArrojarError("El máximo de noches es 14")
		Devolver []
	FIN SI

	SI capacidad < 1 ENTONCES
		ArrojarError("El mínimo de capacidad es de 1 persona")
		Devolver []
	FIN SI

	SI capacidad > 4 ENTONCES
		ArrojarError("El máximo de capacidad es de 4 personas")
		Devolver []
	FIN SI 

	//PASO 3: Cargar universo de habitaciones activas.
	habitaciones <- obtenerHabitacionesActivas()
	SI habitaciones ==  NULL ENTONCES
		Devolver []
	FIN SI

	disponibles <- []

	//PASO 4: Filtrar por capacidad y solapes.

	PARA CADA hab EN habitaciones HACER
		SI hab.capacidad < capacidad ENTONCES
			CONTINUAR //pasar a la siguiente habitación.
		FIN SI

		reservasActivas <- listarReservas (hab.id, estados ∈ {"confirmed","pending"})

		solapa <- FALSO
		PARA CADA r EN reservasActivas HACER
			SI (r.fecha_check_out ≥ fecha_check_in o r.fecha_check_in ≤ fechafecha_check_out) ENTONCES
				solapa <- VERDADERO
				SALIR //cortar evaluación de reservas de esta habitación.
			FIN SI
		FIN PARA
		SI NO solapa ENTONCES
			(agregar(disponibles, hab)
		FIN SI
	FIN PARA


	//PASO 5: Devolver disponibles.

	DEVOLVER disponibles
FIN PROCESO
```
