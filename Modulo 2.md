## 4.2 Módulo 2: Registro de reserva

### Objetivo
Registrar una nueva reserva para una habitación seleccionada por el usuario.  
Se almacena la información del huésped, el rango de fechas, la cantidad de personas y se genera un número único de reserva.  
El estado inicial de la reserva es **`pending`**.

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
- La habitación no debe tener solapamiento con otra reserva *pending* o *confirmed*.  
- Los datos del huésped deben estar completos y válidos.  
- Al registrar la reserva, la habitación queda bloqueada para ese rango de fechas (por *X minutos*).

---

### Salida
- **reserva_id**: número/código único generado.  
- **Estado inicial**: `"pending"`  
- **Monto estimado** = *(tarifa base × noches × cantidad huéspedes + impuestos estimados)*  
- Se registra el huésped si no existía.  
- Se asocia la habitación a la reserva.

---

### Algoritmo
1. Validar fechas, cantidad de huéspedes y formato de datos.  
2. Verificar disponibilidad actual de la habitación (sin solapamientos).  
3. Validar existencia de la habitación y su capacidad.  
4. Crear registro de huésped (si no existe).  
5. Crear nueva reserva en estado `"pending"`.  
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
   4.1 Guardar checkin_date, checkout_date, estado = `"pending"`  
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
     - Estado = `"pending"`  
     - Fechas  
     - Habitación y huésped vinculados  
   - Agregar a la lista de reservas activas  

5. **Salida**
   - Mostrar: ID de reserva, estado = `"pending"`, monto estimado  
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
  estado: "pending" 
} 
AGREGAR_A_LISTA_RESERVAS(reserva) 
// Calcular monto estimado 
monto ← CALCULAR_MONTO(habitacion.tarifa, checkin_date, checkout_date, 
cantidad_huespedes) 
// Salida
