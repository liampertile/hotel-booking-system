# Sistema de Gestión Hotelera

## Índice

1. [Relevamiento, Análisis y Diseño del Sistema](#1-relevamiento-análisis-y-diseño-del-sistema)
   - [1.1 Relevamiento](#11-relevamiento)
   - [1.2 Análisis](#12-análisis)
   - [1.3 Diseño del Sistema](#13-diseño-del-sistema)
   - [1.4 Objetivo General](#14-objetivo-general)
2. [DER (Diagrama entidad-relación)](#2-der-diagrama-entidad-relación)
3. [DFD (Diagrama de flujo de datos)](#3-dfd-diagrama-de-flujo-de-datos)
   - [3.1 Sistema en general](#31-sistema-en-general)
   - [3.2 Módulos](#32-módulos)
     - [3.2.1 Módulo 1](#321-módulo-1)
     - [3.2.2 Módulo 2](#322-módulo-2)
     - [3.2.3 Módulo 3](#323-módulo-3)
     - [3.2.4 Módulo 4](#324-módulo-4)
     - [3.2.5 Módulo 5](#325-módulo-5)
     - [3.2.6 Módulo 6](#326-módulo-6)
   - [3.3 Interpretación global](#33-interpretación-global)
4. [Diagrama de estados](#4-diagrama-de-estados)
5. [Desarrollo de módulos](#5-desarrollo-de-módulos)
   - [Módulo 1](#Módulo-2-consulta-de-disponibilidad)
   - [Módulo 2](#Módulo-2-registro-de-reserva)
   - [Módulo 3](#Módulo-3-confirmación-de-reserva)
   - [Módulo 4](#Módulo-4-preparación-de-la-habitación)
   - [Módulo 5](#Módulo-5-checkin-y-atención-al-huésped)
   - [Módulo 6](#Módulo-6-Checkout-y-liberación-de-la-habitación)

---

## 1. Relevamiento, Análisis y Diseño del Sistema

### 1.1 Relevamiento

En el contexto de la gestión hotelera moderna, se identificó la necesidad de contar con un sistema informático que optimice los procesos vinculados al ciclo completo de la reserva de habitaciones.  
El relevamiento permitió detectar los principales puntos críticos en la operación cotidiana del hotel, como la falta de trazabilidad entre reservas, demoras en la confirmación de pagos y ausencia de un control centralizado sobre la preparación y asignación de habitaciones.

De este estudio preliminar surgieron los requerimientos funcionales esenciales:

- Consultar la disponibilidad de habitaciones en función de fechas, tipo y capacidad, sin alterar los datos operativos.  
- Registrar nuevas reservas asociadas a huéspedes, con validaciones sobre fechas, capacidad y políticas del establecimiento.  
- Confirmar reservas mediante la validación de pagos o garantías de estadía.  
- Gestionar la preparación de habitaciones asegurando el cumplimiento de los estándares de limpieza, mantenimiento y confort.  
- Controlar el proceso de check-in, registrando la ocupación efectiva y habilitando la atención personalizada al huésped.  

Asimismo, se identificó la necesidad de establecer registros históricos que permitan auditar cada operación, garantizando la transparencia y el seguimiento de las acciones realizadas por el personal.

---

### 1.2 Análisis

A partir del relevamiento, se determinaron cinco módulos funcionales que reflejan las etapas clave del ciclo de vida de una reserva hotelera:

- **Consulta de disponibilidad**: permite conocer las habitaciones libres en un rango determinado de fechas, aplicando filtros por tipo y capacidad.  
- **Registro de reserva**: genera una nueva reserva en estado pendiente, asociando los datos del huésped y el detalle de la solicitud.  
- **Confirmación de reserva**: actualiza el estado de la reserva a confirmada una vez verificado el pago o garantía correspondiente.  
- **Preparación de la habitación**: coordina las tareas internas previas al check-in, como limpieza, reposición de insumos y control de mantenimiento.  
- **Check-in y atención al huésped**: formaliza el ingreso del huésped, valida su identidad y marca la habitación como ocupada dentro del sistema.

Junto con un módulo adicional **Check-out y liberación de la habitación** uqe nos permita gestionar de forma adecuada lo qeu respecta a la salida del huésped y la liberación de la habitación, para su posterior preparación.

Los módulos se integran de manera secuencial y dependiente, garantizando que la salida de un proceso constituya la entrada del siguiente.  
Esta estructura minimiza errores operativos y refuerza la coherencia interna del sistema.

Se determinó además la importancia de incorporar reglas de negocio estrictas (validaciones de fechas, capacidades y estados de reserva) para evitar conflictos como sobreasignaciones, reservas duplicadas o habitaciones no preparadas a tiempo.

---

### 1.3 Diseño del Sistema

El sistema fue concebido bajo una arquitectura modular y escalable, en la que cada proceso mantiene independencia lógica, pero se integra dentro de un flujo general coherente.  

Cada módulo se define por los siguientes componentes:

- **Entradas:** datos necesarios para su ejecución (fechas, ID de habitación, datos del huésped, etc.).  
- **Reglas de validación:** restricciones y condiciones de negocio para asegurar la consistencia de la información.  
- **Salidas:** resultados del proceso (estado de la reserva, habitación asignada, comprobante, etc.).  
- **Algoritmo:** secuencia de pasos operativos con distintos niveles de refinamiento.  
- **Pseudocódigo:** representación formal del flujo lógico que facilita la implementación.  

El diseño busca garantizar:

- Trazabilidad completa entre las distintas etapas de una reserva.  
- Integridad de los datos relacionados con huéspedes, habitaciones y transacciones.  
- Secuencialidad y coherencia en la gestión de cada proceso operativo.  
- Facilidad de mantenimiento y extensión futura, permitiendo agregar funcionalidades (check-out, facturación, reportes, etc.) sin alterar la estructura base.

---

### 1.4 Objetivo General

Desarrollar un sistema integral de gestión hotelera que administre de forma ordenada y eficiente el ciclo completo de una reserva —_desde la consulta inicial hasta el check-in_—, garantizando la consistencia de los datos, la eficiencia operativa y una experiencia fluida tanto para el huésped como para el personal del hotel.  

El sistema busca modernizar la operatoria interna, reducir errores humanos y establecer una base sólida para futuras mejoras tecnológicas, como la integración con posibles neuvos módulos.

---

## 2. DER (Diagrama entidad-relación)

El Diagrama Entidad–Relación (DER) define la estructura lógica de los datos que componen el sistema de gestión hotelera. Este modelo permite visualizar las entidades principales del sistema, sus atributos y las relaciones existentes entre ellas, asegurando la integridad y consistencia de la información a lo largo de todo el proceso operativo.

![DER MOD1](./DER%20actualizado.png)

El diseño presentado contempla cinco entidades principales:

- **Persona:** almacena los datos personales y de contacto tanto de huéspedes. Incluye campos como nombre, DNI, correo electrónico y teléfono.  
- **Reserva:** representa el núcleo del sistema. Registra las operaciones de reserva de habitaciones, vinculando un huésped con una habitación durante un rango de fechas determinado. Contiene información como el estado (pendiente, confirmado), el monto total, las fechas de check-in/check-out y referencias a la habitación y al cliente.  
- **Habitación:** modela las unidades físicas del hotel. Cada registro posee atributos de capacidad, tarifa, estado actual (libre, ocupada, preparada, en preparación) y fecha de habilitación. Además, incluye una relación hacia la entidad Reserva, permitiendo conocer qué reserva está asociada actualmente a cada habitación.  
- **Pago:** almacena la información de los pagos efectuados para confirmar reservas. Cada pago se vincula a una reserva específica e incluye monto, moneda, método de pago, estado (autorizado, capturado, reintegrado, anulado) y la fecha de creación. Esta entidad garantiza trazabilidad en las transacciones y permite registrar múltiples pagos por una misma reserva si fuera necesario.
- **Tarea:** representa las actividades operativas relacionadas con la preparación de las habitaciones (limpieza, reposición, mantenimiento). Incluye fechas de asignación, inicio, finalización y validación, así como referencias al miembro del staff responsable y al validador. Además, está directamente asociada a la Habitación, lo que permite gestionar el estado operativo previo al check-in. El estado (pendiente, en progreso y finalizado). El campo validada puede ser de tipo “noValidada”, “bienHecha” o “malHecha”.
- **Staff:** Hace referencia al personal del hotel, contiene los datos personales (nombre, dni), el estado en el que se encuentran (ocupado o no) y el tipo de personal (limpieza, administración).

Relaciones principales:

- Una Persona puede generar muchas Reservas (1:N).  
- Una Reserva está asociada a una sola Habitación, pero una habitación puede tener muchas Reservas a lo largo del tiempo (N:1).  
- Una Reserva puede estar vinculada con uno o más Pagos (1:N).  
- Una Habitación puede tener muchas Tareas asignadas (1:N), las cuales son ejecutadas y validadas por el staff.  

El modelo refleja un esquema relacional normalizado que favorece la integridad referencial y evita redundancias. El diseño también permite futuras extensiones, como la incorporación de entidades de Check-out, Facturación, Servicios adicionales o Reportes estadísticos, manteniendo la misma lógica estructural y la coherencia de los datos.


---

## 3. DFD (Diagrama de flujo de datos)

### 3.1 Sistema en general

![DER MOD1](./DFD%20COMPLETO.png)

El DFD general (nivel 0) presenta una visión integrada de los cinco procesos que conforman el ciclo operativo del sistema hotelero.  
Cada proceso se encuentra interconectado de forma lógica, evidenciando la dependencia secuencial entre los módulos: desde la consulta inicial hasta el check-in efectivo del huésped.

Principales flujos identificados:

- La **interacción con el huésped**, que inicia el proceso al consultar disponibilidad y culmina con la notificación de check-in exitoso.
- Los **procesos administrativos**, donde el personal del hotel y el sistema de pagos gestionan las operaciones críticas de confirmación, limpieza y ocupación.
- Las **bases de datos centrales** —_Habitación, Reserva, Pago, Persona y Tarea_— que actúan como repositorios intermedios garantizando la persistencia y validación de la información.

Este nivel permite comprender el **funcionamiento global del sistema como un ecosistema integrado**, donde cada módulo realiza una función específica y contribuye a mantener la coherencia del flujo operativo.

---

### 3.2 Módulos

#### 3.2.1 Módulo 1

Representa el punto de partida del proceso de reservas.  
El huésped ingresa un rango de fechas y la cantidad de huéspedes. El sistema consulta las bases de datos y devuelve habitaciones disponibles.

- **Entradas:** fechas, cantidad de huéspedes.  
- **Salidas:** listado filtrado de habitaciones disponibles.  
- **Almacenamientos:** Habitación, Reserva.
  
El proceso no genera modificaciones ni bloqueos de datos, respetando el principio de no mutación del sistema en la etapa de consulta.

![DER MOD1](./Modulo1/DFD%20MODULO%201.png)


---

#### 3.2.2 Módulo 2

Crea una reserva preliminar (estado `pendiente`).  
El huésped ingresa sus datos y selecciona una habitación disponible. Se verifica solapamiento, se registra el huésped si no existe y se crea la reserva temporal.

- **Entradas:** datos del huésped, habitación seleccionada.  
- **Salidas:** confirmación provisional, número de reserva.  
- **Almacenamientos:** Persona, Habitación, Reserva. 

Este módulo inicia la persistencia de datos, ya que introduce registros nuevos que serán validados en los siguientes procesos.

![DER MOD1](./Modulo2/DFD%20MODULO%202.png)

---

#### 3.2.3 Módulo 3

Formaliza la reserva mediante la validación del pago.  
Si el pago se aprueba, se actualiza la reserva a `confirmada` y la habitación a reservada.

- **Entradas:** datos de pago, reserva pendiente.  
- **Salidas:** comprobante de confirmación, actualización de estado.  
- **Almacenamientos:** Pago, Reserva, Habitación.

Este módulo es clave porque consolida la coherencia financiera y operativa del proceso, garantizando que solo reservas con pago válido avancen al siguiente paso.

![DER MOD1](./Modulo3/DFD%20MODULO%203.png)

---

#### 3.2.4 Módulo 4

Gestiona el flujo interno de preparación de habitaciones.  
Tras la confirmación de reserva, se generan tareas (limpieza, mantenimiento, reposición) a completar antes del check-in.

- **Entradas:** confirmación de reserva, personal disponible.  
- **Salidas:** habitación marcada como preparada.  
- **Almacenamientos:** Tarea, Habitación, Reserva.

El proceso promueve la gestión de calidad interna, permitiendo al hotel mantener un registro digital del estado de las tareas y el cumplimiento de los plazos operativos.

![DER MOD1](./Modulo4/DFD%20MODULO%204.png)

---

#### 3.2.5 Módulo 5

Etapa final del ciclo operativo (check-in).  
El huésped se presenta con su documento y número de reserva; el sistema valida y actualiza estados a `ocupada` y `confirmado`.

- **Entradas:** reserva confirmada, identificación del huésped.  
- **Salidas:** notificación de check-in exitoso, habitación ocupada.  
- **Almacenamientos:** Reserva, Habitación.

Este proceso cierra el flujo de la reserva garantizando consistencia entre la información administrativa y la ocupación real.

![DER MOD1](./Modulo5/DFD%20MODULO%205.png)

---

#### 3.2.6 Módulo 6

El diagrama de flujo de datos del Módulo 6 – Check-out representa la etapa final del ciclo operativo del sistema.
El proceso se ejecuta una vez que el huésped ha completado su estadía.
El personal del hotel activa el procedimiento de check-out, que tiene como propósito liberar la habitación, finalizar la reserva y preparar la unidad para el próximo ingreso.

- **Entradas:**
   - Identificador de habitación (habitacion_id)
   - Identificador de reserva (reserva_id)
   - Orden del staff para ejecutar el check-out

- **Procesos:**
  - Liberar habitación:cambia el estado de la habitación de ocupada a libre.  
  - Finalizar reserva: actualiza el estado de la reserva a finalizada.  
  - Preparar habitación: invoca el módulo de Preparación de Habitación para reestablecer el estado y las tareas asociadas.
     
- **Salidas:**
   - Habitación en estado libre y disponible para una nueva reserva.
   - Reserva actualizada como finalizada.
   - Confirmación de check-out enviada al staff.

- **Almacenamientos:**
   - Habitación: refleja el cambio de estado a libre.
   - Reserva: guarda el estado finalizada.
   - Tarea: se activa el proceso de Preparación de Habitación.
 
Descripción general:
Este módulo completa el ciclo operativo del sistema hotelero.
A partir de la acción del personal, se sincronizan los estados administrativos y físicos: la habitación se libera, la reserva se cierra y el proceso de limpieza y acondicionamiento vuelve a dejar la unidad lista para una nueva ocupación.
De esta manera, se garantiza la continuidad del flujo y la coherencia entre la información almacenada y el estado real de las instalaciones.
  
![DER MOD1](./Modulo6/DFD%20MODULO%206.png)

---

### 3.3 Interpretación global

Los DFD demuestran cómo el sistema opera de forma modular, segura y controlada.  
Cada flujo garantiza una transformación válida de datos: entrada → procesamiento → salida.  

Además, la descomposición progresiva permite:

- Identificar puntos críticos (pagos, validaciones).  
- Mantener una visión jerárquica del flujo de información.  
- Alinear el modelo funcional (DFD) con el modelo de datos (DER).

---
## 4. Diagrama de estados
El siguiente diagrama de estados resume el ciclo de vida completo de una reserva dentro del sistema de gestión hotelera.  
Integra las transiciones entre los distintos módulos operativos —desde la consulta de disponibilidad hasta el check-out— reflejando cómo los estados de **habitaciones** y **reservas** evolucionan de forma sincronizada.

<p align="center">
  <img src="./diagrama_estado.png" alt="Diagrama de estados del sistema" width="900">
</p>

### Interpretación

El modelo muestra un flujo continuo y cerrado de operaciones que garantiza la coherencia entre los procesos administrativos y operativos del hotel:

- **Inicio del ciclo:** el huésped consulta la disponibilidad (`Consulta_Disponibilidad`) y selecciona una habitación.  
  Este estado inicial no altera datos, solo filtra opciones según capacidad y fechas.

- **Creación de reserva:** tras la selección, el sistema genera una **reserva en estado `pendiente`** (`Registro_Reserva`), asegurando el bloqueo temporal de la habitación mientras se espera la confirmación del pago.

- **Confirmación de reserva:** una vez capturado o autorizado el pago (`Confirmacion_Reserva`), la reserva pasa a estado **`confirmada`**, habilitando la fase operativa de preparación.

- **Preparación de habitación:** el módulo interno (`Preparacion_Habitacion`) gestiona tareas como limpieza, mantenimiento o reposición.  
  Este subproceso controla los estados **`En_Preparacion`** y **`Preparada`**, evitando que se asigne una habitación sin validar.

- **Check-in:** cuando la habitación está lista, el huésped realiza el ingreso y la reserva cambia a **`confirmado`**.  
  Este paso consolida la ocupación efectiva y marca el inicio de la estadía.

- **Check-out:** al finalizar la estadía, el staff ejecuta el cierre del ciclo.  
  La habitación se libera, la reserva pasa a **`finalizada`**, y se re-invoca el proceso de preparación, garantizando la continuidad del flujo operativo.

### Observaciones

Este modelo permite visualizar:

- La **dependencia jerárquica** entre los módulos del sistema (cada estado habilita el siguiente).  
- El **control transaccional** de cada etapa, asegurando que ninguna habitación avance a un estado inconsistente.  
- La **reutilización de subprocesos** (como la preparación de habitación) en distintos contextos del ciclo.  
- Una arquitectura **determinística y trazable**, ideal para implementar mediante máquinas de estados o controladores por eventos.

En conjunto, el diagrama valida que el sistema mantiene **integridad operacional** en todo momento, alineando las acciones del huésped, el staff y la base de datos dentro de un mismo flujo lógico.


## 5. Desarrollo de módulos

## Módulo 1 Consulta de disponibilidad

### Objetivo

Determinar qué habitaciones están libres en un rango de fechas `[fecha_check_in, fecha_check_out)` sin modificar el estado del sistema ni generar bloqueos o reservas.

### Entradas

- **fecha_check_in** _(fecha)_: inclusive, es decir, ese día la habitación debe estar libre.
- **fecha_check_out** _(fecha)_: exclusivo, ya que ese día el huésped se retirará de la habitación.
- **cantidad_huest** _(número)_: indica el número de huéspedes que albergará la habitación.

### Reglas y validaciones

- Fechas válidas: `fecha_check_in` < `fecha_check_out` y `fecha_check_in` > `fecha_actual()`. 
- La capacidad de la habitación debe ser igual o mayor a la capacidad ingresada por el usuario.
- No mutación de estado: la consulta no crea, bloquea o actualiza reserva ni tareas. 
- Límites del rango: el máximo de noches son 14, por lo tanto, se debe validar el tamaño del intervalo. 

### Salidas

- Lista de habitaciones disponibles, con los campos mínimos: **`id`**, **`capacidad`**, **`tarifa`**.
- Sin efectos laterales: no crea ni modifica reservas/bloqueos.

### Algoritmo

1. Usuario ingresa capacidad, fecha_check_in y fecha_check_out. 
2. Validar entradas: fechas, límites de noches (≤ 14) y capacidad (≥ 1 𝑦 ≤ 4). 
3. Cargar universo de habitaciones activas. 
4. Filtrar habitaciones disponibles y sin solapes, cuya capacidad sea mayor o igual a la solicitada por el usuario. 
5. Construir la lista de disponibles con las habitaciones sin solapes.
6. Devolver la lista de habitaciones disponibles (sin mutaciones).


### Refinamiento - Nivel 1

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

### Refinamiento - Nivel 2

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
			SI NO (r.fecha_check_out ≤ fecha_check_in O r.fecha_check_in ≥ fechafecha_check_out) ENTONCES
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


## Módulo 2 Registro de reserva

### Objetivo
Registrar una nueva reserva para una habitación seleccionada por el usuario.  
Se almacena la información del huésped, el rango de fechas, la cantidad de personas y se genera un número único de reserva.  
El estado inicial de la reserva es **`pendiente`**.

---

### Entradas
- **habitacion_id** *(número)*: ID de la habitación seleccionada.  
- **checkin_date** *(Date)*: Fecha de entrada (inclusive).  
- **checkout_date** *(Date)*: Fecha de salida (exclusiva).  
- **cantidad_huespedes** *(entero)*: Número de personas a alojar.  
- **huesped** *(objeto)*:
  - nombre *(string)*
  - documento *(string)*
  - email *(string)*
  - telefono *(string)*

---

### Reglas y validaciones
- La fecha de check-in debe ser anterior a la de check-out.  
- El rango máximo es de **14 noches**.  
- La habitación debe existir, estar activa y tener capacidad suficiente.  
- La habitación no debe tener solapamiento con otra reserva *pendiente* o *confirmada*.  
- Los datos del huésped deben estar completos y válidos.  
- Al registrar la reserva, la habitación queda bloqueada para ese rango de fechas (por *X minutos*).

---

### Salida
- **reserva_id**: número/código único generado.  
- **Estado inicial**: `"pendiente"`  
- **Monto estimado** = *(tarifa base × noches × cantidad huéspedes + impuestos estimados)*  
- Se registra el huésped si no existía.  
- Se asocia la habitación a la reserva.

---

### Algoritmo
1. Validar fechas, cantidad de huéspedes y formato de datos.  
2. Verificar disponibilidad actual de la habitación (sin solapamientos).  
3. Validar existencia de la habitación y su capacidad.  
4. Crear registro de huésped (si no existe).  
5. Crear nueva reserva en estado `"pendiente"`.  
6. Asociar habitación a la reserva.  
7. Devolver ID de reserva y estado.

---

### Refinamiento - Nivel 1
1. **Validar entradas:**
   1.1 Check-in < Check-out  
   1.2 Diferencia de días ≤ 14  
   1.3 Cantidad de huéspedes ≥ 1  
   1.4 Datos del huésped no vacíos  
2. **Verificar habitación:**
   2.1 Existe  
   2.2 Capacidad ≥ cantidad de huéspedes  
   2.3 No tiene reservas activas solapadas  
3. **Registrar huésped si no existe**  
4. **Crear reserva:**
   4.1 Guardar checkin_date, checkout_date, estado = `"pendiente"`  
   4.2 Asignar huesped_id y habitacion_id  
5. **Calcular y mostrar monto estimado**

---

### Refinamiento - Nivel 2
1. **Validar fechas**
   - Si checkin ≥ checkout → Error  
   - Si noches > 14 → Error  
   - Si cantidad huéspedes < 1 → Error  

2. **Validar habitación**
   - Buscar habitación por habitacion_id  
   - Si no existe → Error  
   - Si capacidad < cantidad_huespedes → Error  
   - Buscar en reservas activas si hay solapamiento → Si hay → Error  

3. **Validar huésped**
   - Verificar que nombre, documento, email, teléfono ≠ vacío  
   - Si huésped con mismo documento ya existe → reutilizar huesped_id  

4. **Registrar reserva**
   - Crear objeto reserva con:
     - ID generado  
     - Estado = `"pendiente"`  
     - Fechas  
     - Habitación y huésped vinculados  
   - Agregar a la lista de reservas activas  

5. **Salida**
   - Mostrar: ID de reserva, estado = `"pendiente"`, monto estimado  
   - La habitación queda bloqueada temporalmente  

---

### Pseudocódigo
```pseudo
INICIO REGISTRAR_RESERVA 
LEER habitacion_id, checkin_date, checkout_date, cantidad_huespedes 
LEER nombre, documento, email, telefono 
// Validar fechas 
SI checkin_date ≥ checkout_date ENTONCES 
  MOSTRAR "Error: Fechas inválidas" 
  TERMINAR 
FIN SI 
SI DIAS_ENTRE(checkin_date, checkout_date) > 14 ENTONCES 
  MOSTRAR "Error: Máximo 14 noches permitidas" 
  TERMINAR 
FIN SI 
// Validar habitación 
habitacion ← BUSCAR_HABITACION(habitacion_id) 
SI habitacion = NULO ENTONCES 
  MOSTRAR "Error: Habitación inexistente" 
  TERMINAR 
FIN SI 
SI habitacion.capacidad < cantidad_huespedes ENTONCES 
  MOSTRAR "Error: Capacidad insuficiente" 
  TERMINAR 
FIN SI

SI EXISTE_SOLAPAMIENTO(habitacion_id, checkin_date, checkout_date) 
ENTONCES 
  MOSTRAR "Error: Habitación no disponible en ese rango" 
  TERMINAR 
FIN SI 
// Verificar o crear huésped 
huesped ← BUSCAR_HUESPED(documento) 
SI huesped = NULO ENTONCES 
huesped ← CREAR_HUESPED(nombre, documento, email, telefono) 
FIN SI 
// Crear reserva 
reserva_id ← GENERAR_ID_UNICO() 
reserva ← { 
  id: reserva_id, 
  huesped_id: huesped.id, 
  habitacion_id: habitacion.id, 
  checkin_date: checkin_date, 
  checkout_date: checkout_date, 
  estado: "pendiente" 
} 
AGREGAR_A_LISTA_RESERVAS(reserva) 
// Calcular monto estimado 
monto ← CALCULAR_MONTO(habitacion.tarifa, checkin_date, checkout_date, 
cantidad_huespedes) 
// Salida
```


## Módulo 3 Confirmación de Reserva

## Objetivo

Confirmar una reserva existente mediante el registro de un pago válido.  
El proceso asegura que la reserva esté activa, que el importe sea correcto, que el pago quede debidamente registrado y que, si el pago fue efectivamente capturado, la reserva cambie su estado de `pendiente` a `confirmada`.

---

## Entradas

- **reserva_id (número):** Identificador único de la reserva a confirmar.  
- **monto (número):** Importe abonado por el cliente.  
- **moneda (string):** Tipo de moneda utilizada (por ejemplo, `ARS`).  
- **metodo_pago (string):** Medio de pago empleado (tarjeta, efectivo, transferencia, etc.).  
- **estado (string):** Estado del pago (`autorizado`, `capturado`, `anulado`).  
- **staff_id (número):** Identificador del empleado (tipo *staff*) responsable de la confirmación.

---

## Reglas y Validaciones

1. La reserva debe existir y encontrarse en estado `pendiente`.  
2. Solo pueden confirmarse reservas que no estén canceladas ni completadas.  
3. El monto del pago debe ser mayor que cero.  
4. El estado del pago debe ser uno de los válidos: `autorizado`, `capturado`, o `anulado`.  
5. Todo pago registrado debe incluir método, monto, moneda, estado y fecha de creación.  
6. Si el pago fue capturado, la reserva cambia automáticamente a estado `confirmada`.  
7. Si el pago no fue capturado, la reserva permanece `pendiente`.

---

## Salida

- Estado final de la reserva (`confirmada` si el pago fue capturado; `pendiente` si no).  
- Registro del pago con los campos: monto, moneda, método, estado y fecha de creación.  
- Fecha y usuario que confirmaron la reserva (solo si fue capturada).  
- Mensaje informativo con el resultado del proceso.

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
```
## Módulo 4 Preparación de la habitación

### Objetivo

En este módulo se trabaja la preparación de la habitación, previa al check-in e ingreso de un nuevo huésped. Cada actividad involucrada en dejar la habitación preparada deberá realizarse por 1 persona asignada, cumpliendo con un plazo de tiempo definido: debe ser realizada previa al horario en el que se realiza la entrada a la habitación de un nuevo huésped. Las tareas que se deben realizar para dejar la habitación preparada son `Limpiar los pisos`, `Cambiar sábanas y toallas` y `Reponer el frigobar`. Cuando cada tarea presenta `estado = "finalizado"` y se encuentra validada, la habitación puede ser habilitada para ser ocupada.

### Entradas

- **reserva_id** _(número)_: Identificador único de la reserva.
- **user_id** _(número)_: Identificador único del usuario que realizó la reserva.
- **habitacion_id** _(número)_: Identificador único de la habitación asociada a la reserva.

### Reglas y validaciones

- La habitación debe existir y estar asociada a una reserva válida.
- La **fecha de check-in** debe ser posterior a la fecha actual.
- La habitación **no debe estar ocupada** ni en mantenimiento.
- Si la habitación ya se encuentra **en estado "preparada"**, no se vuelve a preparar.
- Todas las tareas deben reiniciarse antes de comenzar el proceso (`estado = pendiente`, `validada = FALSO`).
- Solo se pueden asignar tareas a **personal con estado "disponible"**.
- El número de personas disponibles debe ser **mayor o igual al número de tareas**.
- Cada tarea debe tener **un único responsable asignado**.
- Solo pueden iniciarse tareas en estado `"pendiente"`.
- Solo pueden finalizarse tareas en estado `"enProgreso"`.
- Solo pueden validarse tareas en estado `"finalizada"`.
- Cada tarea validada debe tener una `fecha_validación ≤ fecha_check_in`.
- La habitación se marca como **"preparada"** solo cuando todas las tareas están validadas a tiempo.
- Si alguna tarea no se valida antes del check-in, se retrasa el ingreso y se reabre la validación.

### Salidas

- Habitación con estado **`preparada`** y lista para el ingreso del nuevo huésped.

### Algoritmo

1. Realizar comprobaciones de la habitación.
2. Reestablecer estado de preparación de la habitación.
3. Asignar tareas de preparación a personal disponible.
4. Gestionar ejecución de tareas.
5. Verificar que todas las tareas estén validadas para preparar la habitación.


### Refinamiento - Nivel 1


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

### Refinamiento - Nivel 2

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

### Pseudocódigo

```pseudo
PROCESO PrepararHabitación(habitacion_id, reserva_id, user_id):
	ComprobarHabitación(habitacion_id, reserva_id, user_id)
   	ReestablecerEstado(habitacion_id)
   	AsignarTareas(habitacion_id)
   	GestionarTareas(habitacion_id)
   	VerificarValidación(reserva_id, habitacion_id)
FIN PROCESO

PROCESO ComprobarHabitación(habitacion_id, reserva_id, user_id):
	ComprobarEstado(habitacion_id)
	ComprobarReserva(reserva_id, user_id)
   	ComprobarOcupación(habitacion_id)
FIN PROCESO

PROCESO ComprobarEstado(habitacion_id):
	habitacion <- obtenerHabitacionPorId(habitacion_id)
	SI habitacion.estado == "preparada"
		imprimir("La habitación ya se encuentra preparada, no se preparará nuevamente")
	SINO
		imprimir("La habitación no se encuentra preparada")
	FIN SI
FIN PROCESO

PROCESO ComprobarReserva(reserva_id, user_id):
	reserva <- obtenerReservaPorId(reserva_id)
	SI reserva.fecha_check_in > fecha_actual Y reserva.estado == "confirmada" Y reserva.cliente_id == user_id ENTONCES
		imprimir("La habitación tiene una próxima reserva")
	SINO
		imprimir("La habitación no tiene una próxima reserva")
	FIN SI
FIN PROCESO

PROCESO ComprobarOcupacion(habitacion_id):
	habitacion <- obtenerHabitacionPorId(habitacion_id)
	SI habitacion.estado == "ocupada" ENTONCES
		imprimir("La habitación se encuentra ocupada, no se procede a preparar")
	SINO
		imprimir("La habitación se encuentra desocupada, se procede a preparar")
	FIN SI
FIN PROCESO

PROCESO ReestablecerEstado(habitacion_id):
	habitacion <- obtenerHabitacionPorId(habitacion_id)
	listaDeTareas <- habitacion.tareas
	PARA cada tarea en listaDeTareas:
		tarea.estado <- "pendiente"
		tarea.validada <- "noValidada"
	FIN PARA
	habitacion.estado <- "libre"
	habitacion.tareas <- listaDeTareas
FIN PROCESO

PROCESO AsignarTareas(habitacion_id):
	habitacion <- obtenerHabitacionPorId(habitacion_id)
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

PROCESO GestionarTareas(habitacion_id):
	IniciarTarea(habitacion_id)
   	FinalizarTarea(habitacion_id)
   	ValidarTarea(habitacion_id)
FIN PROCESO

PROCESO VerificarValidación(reserva_id, habitacion_id)
	todasValidadas <- VERDADERO
	habitacion <- obtenerHabitacionPorId(habitacion_id)
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

PROCESO EstablecerHabitaciónPreparada(habitacionId)
	habitacion <- obtenerHabitacionPorId(habitacion_id)
   	habitacion.estado <- "preparada"
   	habitacion.fecha_habitacion_habilitada <- fecha_actual
   	imprimir("Habitación lista para check-in")
FIN PROCESO

PROCESO IniciarTarea(habitacionId)
   	tarea <- seleccionarTarea(habitacionId, "pending")
   	SI tarea ≠ NULL ENTONCES
      tarea.estado ← "inProgress"
      tarea.fecha_inicio ← fecha_actual
      imprimir("Tarea " + tarea.id + " iniciada.")
   	SINO
      imprimir("No hay tareas pendientes para iniciar.")
   	FIN SI
FIN PROCESO

PROCESO FinalizarTarea(habitacionId)
   	tarea <- seleccionarTarea(habitacionId, "inProgress")
   	SI tarea ≠ NULL ENTONCES
      tarea.estado <- "finalizada"
      tarea.fecha_fin ← fecha_actual
      imprimir("Tarea " + tarea.id + " finalizada.")
   	SINO
      imprimir("No hay tareas en progreso para finalizar.")
   	FIN SI
FIN PROCESO

PROCESO ValidarTarea(habitacionId)
   	tarea <- seleccionarTarea(habitacionId, "finished")
   	SI tarea ≠ NULL ENTONCES
      tarea.fecha_validacion <- fecha_actual
	   tarea.validada <- leer(validacion)
      imprimir("Tarea " + tarea.id + " validada correctamente.")
   	SINO
      imprimir("No hay tareas finalizadas para validar.")
   	FIN SI
FIN PROCESO
```




## Módulo 5 Checkin y atención al huésped

### Objetivo
Formalizar la llegada del huésped y marcar la ocupación real de la habitación. Este proceso debe asegurar que la reserva esté confirmada, la habitación esté preparada y se realice dentro del rango de la fecha de check-in.

---

### Entradas

- **reserva_id** *(número)*: Identificador único de la reserva para realizar el check-in.
- **identificacion_huesped** *(string)*: Documento de identidad presentado por la persona que se presenta para el check-in.
  
---

### Reglas y validaciones

- La reserva identificada por `reserva_id` debe existir.
- La reserva debe estar en estado **"confirmed"**.
- La habitación asociada a la reserva debe estar en estado **"preparada"**.
- El check-in debe realizarse en la fecha de check-in registrada en la reserva o en una fecha cercana (dentro de un rango de tolerancia, por ejemplo, el mismo día).
- La identificación presentada (`identificacion_huesped`) debe coincidir con el DNI del huésped titular de la reserva.
- El proceso debe modificar el estado de la habitación a **"ocupada"**.
  
---

### Salida

- La reserva asociada a la habitación queda ocupada.
- La habitación cambia su estado a **"ocupada"**.
- Mensaje informativo con el resultado del proceso.
  
---

### Algoritmo

1. Validar la existencia de la reserva y su estado (debe ser **"confirmed"**).
2. Verificar la identidad del huésped, comparando la identificación presentada con la registrada en la reserva.
3. Verificar que la habitación asociada esté en estado **"preparada"**.
4. Comprobar que la operación se realice dentro de la fecha de check-in permitida.
5. Actualizar el estado de la habitación a **"ocupada"**.
6. Vincular la reserva a la habitación como la ocupación actual.
7. Retornar el estado de la operación y la confirmación de la ocupación.
   
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
   * 1.1. Buscar la reserva utilizando el `reserva_id`.
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

### Pseudocodigo

```pseudo
INICIO CHECK_IN(reserva_id, identificacion_huesped)

reserva ← BUSCAR_RESERVA(reserva_id)
SI reserva = NULO ENTONCES
    MOSTRAR "Error: Reserva inexistente"
    TERMINAR
FIN SI

SI reserva.estado ≠ "confirmed" ENTONCES
    MOSTRAR "Error: La reserva no está confirmada"
    TERMINAR
FIN SI

huesped ← BUSCAR_HUESPED(reserva.huesped_id)
SI huesped.dni ≠ identificacion_huesped ENTONCES
    MOSTRAR "Error: La identificación no coincide con el titular"
    TERMINAR
FIN SI

habitacion ← BUSCAR_HABITACION(reserva.habitacion_id)
SI habitacion.estado ≠ "preparada" ENTONCES
    MOSTRAR "Error: La habitación no está lista para el check-in"
    TERMINAR
FIN SI

SI FECHA_ACTUAL < reserva.fecha_check_in ENTONCES
    MOSTRAR "Error: Check-in anticipado no permitido"
    TERMINAR
FIN SI

habitacion.estado ← "ocupada"

MOSTRAR "Check-in realizado. Habitación " + habitacion.id + " ocupada."

FIN
```



## Módulo 6 Checkout y liberación de la habitación

### Objetivo

Gestionar la salida del huésped y liberar la habitación para su posterior limpieza y preparación.  
El proceso debe asegurar que la reserva esté activa, que la habitación esté actualmente ocupada y que el procedimiento se realice de manera controlada, dejando la habitación en estado **`libre`** y lista para el servicio de limpieza.

---

### Entradas

- **habitacion_id** _(número)_: Identificador único de la habitación que se desea liberar.  
- **reserva_id** _(número)_: Identificador único de la reserva asociada al huésped que realiza el check-out.

---

### Reglas y validaciones

- La habitación identificada por `habitacion_id` debe existir.  
- La reserva identificada por `reserva_id` debe existir.  
- La habitación debe estar en estado **`ocupada`**.  
- La reserva asociada debe estar en estado **`confirmada`** o **`en curso`**.  

Una vez realizado el check-out:

- Se actualiza el estado de la habitación a **`libre`**.  
- Se actualiza el estado de la reserva a **`finalizada`**.  
- Se ejecuta el proceso de preparación de habitación (`PrepararHabitación(habitacion_id, reserva_id)`) para dejarla lista para el próximo huésped.

---

### Salidas

- La habitación queda liberada (**estado = "libre"**).  
- La reserva pasa al estado **`finalizada`**.  
- Se ejecuta el proceso de limpieza y preparación (`PrepararHabitación(habitacion_id, reserva_id)`).  
- Se genera un mensaje informativo con el resultado del proceso y la hora exacta del check-out registrado.

---

### Algoritmo

1. Se libera la habitación.
2. Se finaliza la reserva.
3. Se prepara la habitación.

### Refinamiento - Nivel 1

1. Se libera la habitación.
   * 1.1 Actualizar estado de la habitación.
2. Se finaliza la reserva.
  * 2.1 Actualizar estado de la reserva.
3. Se prepara la habitación.
  * 3.1 Ejecutar PrepararHabitación(habitacion_id, reserva_id).

### Refinamiento - Nivel 2

1. Se libera la habitación.
  * 1.1 Actualizar estado de la habitación.
  * 1.2 Obtener la habitación por id.
  * 1.3 Si la habitación no existe → Mostrar "Habitación inexistente".
  * 1.4 Sino:
       - Si el estado de la habitación es "ocupado" → Cambiar el estado a "libre".
       - Sino → Mostrar "La habitación no se encuentra ocupada".

2. Se finaliza la reserva.
  * 2.1 Actualizar estado de la reserva.
  * 2.2 Obtener la reserva por id.
  * 2.3 Si la reserva no existe → Mostrar "Reserva inexistente".
  * 2.4 Sino:
       - Establecer el estado de la reserva en "finalizada".
       - Registrar la fecha de check-out con la fecha actual.

3. Se prepara la habitación.
  * 3.1 Ejecutar PrepararHabitación(habitacion_id, reserva_id).

### Pseudocódigo

```pseudo

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
		SI habitacion.estado == "ocupado"
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

```
