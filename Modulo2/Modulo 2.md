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
- Los datos del huésped deben estar completos y válidos.
- Se registra el huésped si no existía.   
- Al registrar la reserva, la habitación queda bloqueada para ese rango de fechas (por *X minutos*).

---

### Salida
- **reserva_id**: número/código único generado.  

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
   1.1 fecha_check_in < fecha_check_out 
   1.2 Diferencia de días ≤ 14  
   1.3 Cantidad de huéspedes ≥ 1  
   1.4 Datos del huésped no vacíos  
2. **Verificar habitación:**
   2.1 Existe  
   2.2 capacidad ≥ cantidad de huéspedes  
   2.3 No tiene reservas activas solapadas  
3. **Registrar huésped si no existe**  
4. **Crear reserva:**
   4.1 Guardar fecha_check_in, fecha_check_out, estado = `"pendiente"`  
   4.2 Asignar huesped_id y habitacion_id  
5. **Calcular y mostrar monto estimado**

---

### Refinamiento - Nivel 2
1. **Validar fechas**
   - Si fecha_check_in ≥ fecha_check_out → Error  
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
LEER habitacion_id, fecha_check_in, fecha_check_out, cantidad_huespedes 
LEER nombre, documento, email, telefono 
// Validar fechas 
SI fecha_check_in ≥ fecha_check_out ENTONCES 
  MOSTRAR "Error: Fechas inválidas" 
  TERMINAR 
FIN SI 
SI DIAS_ENTRE(fecha_check_in, fecha_check_out) > 14 ENTONCES 
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

SI EXISTE_SOLAPAMIENTO(habitacion_id, fecha_check_in, fecha_check_out) 
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
  fecha_check_in: fecha_check_in, 
  fecha_check_out: fecha_check_out, 
  estado: "pendiente" 
} 
AGREGAR_A_LISTA_RESERVAS(reserva) 
// Calcular monto estimado 
monto ← CALCULAR_MONTO(habitacion.tarifa, fecha_check_in, fecha_check_out, 
cantidad_huespedes) 
// Salida
