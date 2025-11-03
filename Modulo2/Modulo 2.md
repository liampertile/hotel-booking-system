## Módulo 2: Registro de reserva

### Objetivo
Registrar una nueva reserva para una habitación seleccionada por el usuario.  
Se almacena la información del huésped, el rango de fechas, la cantidad de personas y se genera un número único de reserva.  
El estado inicial de la reserva es **`pendiente`**.

---

### Entradas
- **habitacion_id** *(número)*: ID de la habitación seleccionada.   
- **huesped** *(objeto)*:

---

### Reglas y validaciones
- Al registrar la reserva, la habitación queda bloqueada para ese rango de fechas (por *X minutos*).

---

### Salida
- **reserva_id**: número/código único generado.  

---

### Algoritmo
1. Verificar existencia del huésped.  
2. Si el huésped no existe, crear registro nuevo en la base de datos.  
3. Generar un nuevo `reserva_id`.  
4. Crear registro de reserva con:  
   - `habitacion_id`  
   - `huesped_id`  
   - `estado = "pendiente"`  
5. Bloquear temporalmente la habitación en el rango de fechas asociado.  
6. Devolver `reserva_id` y estado `"pendiente"`.  


---

### Refinamiento - Nivel 1
1. **Comprobar huésped**
   1.1. Buscar huésped por documento.  
   1.2. Si no existe → crear nuevo registro.  
   1.3. Obtener `huesped_id`.

3. **Registrar reserva**
   2.1. Generar `reserva_id` único.  
   2.2. Asignar `habitacion_id` y `huesped_id`.  
   2.3. Establecer `estado = "pendiente"`.  
   2.4. Guardar en la lista de reservas activas.

4. **Bloquear habitación**
   3.1. Marcar habitación como “bloqueada” por X minutos.

5. **Devolver resultados**
   4.1. Mostrar número de reserva y estado inicial.


---

### Refinamiento - Nivel 2
1. **Validar huésped**
   1.1. `huesped ← BUSCAR_HUESPED(documento)`  
   1.2. Si `huesped = NULL` →    `huesped_id ← CREAR_HUESPED(nombre, documento, email, telefono)`  
   1.3. Sino →  `huesped_id ← huesped.id`

2. **Generar reserva**
   2.1. `reserva_id ← GENERAR_ID_RESERVA()`  
   2.2. `estado ← "pendiente"`  
   2.3. `CREAR_RESERVA(reserva_id, habitacion_id, huesped_id, estado)`

3. **Bloquear habitación**
   3.1. `BLOQUEAR_HABITACION(habitacion_id, tiempo = 15 MINUTOS)`

4. **Salida**
   4.1. Mostrar mensaje:  
   “Reserva creada correctamente.”  
   “Número de reserva: ” + reserva_id  
   “Estado inicial: pendiente.”


---

### Pseudocódigo
```pseudo
INICIO MODULO RegistroDeReserva

    // Entradas
    LEER habitacion_id
    LEER huesped.nombre
    LEER huesped.documento
    LEER huesped.email
    LEER huesped.telefono

    // 1. Validar / Registrar huésped
    huesped_existente ← BUSCAR_HUESPED_POR_DOCUMENTO(huesped.documento)

    SI huesped_existente = NULO ENTONCES
        huesped_id ← CREAR_HUESPED(huesped.nombre, huesped.documento,
                                   huesped.email, huesped.telefono)
    SINO
        huesped_id ← huesped_existente.id
    FIN SI

    // 2. Crear nueva reserva
    reserva_id ← GENERAR_ID_RESERVA()
    estado ← "pendiente"
    CREAR_RESERVA(reserva_id, habitacion_id, huesped_id, estado)

    // 3. Bloquear temporalmente la habitación
    BLOQUEAR_HABITACION(habitacion_id, tiempo_bloqueo = 15 MINUTOS)

    // 4. Salida
    MOSTRAR "Reserva registrada exitosamente."
    MOSTRAR "Número de reserva: ", reserva_id
    MOSTRAR "Estado: pendiente"
    MOSTRAR "La habitación ha sido bloqueada temporalmente."

FIN MODULO
