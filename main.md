## Módulo Principal (Main)

### Objetivo

Servir como punto de entrada y controlador principal del sistema. Su función es presentar al usuario un menú de opciones que le permita navegar e invocar los diferentes módulos funcionales (Consulta, Registro, Confirmación, etc.) de manera ordenada. Gestiona el ciclo de vida de la aplicación, manteniéndose en ejecución hasta que el usuario elija explícitamente la opción de salir.

-----

### Entradas

  - **opcion\_usuario** *(entero)*: Número seleccionado por el usuario desde el menú principal para ejecutar un módulo específico.

-----

### Reglas y validaciones

  - El sistema debe mostrar el menú de opciones de forma continua después de completar cada operación.
  - Solo se aceptarán como válidas las opciones numéricas que correspondan a una funcionalidad existente en el menú.
  - Si el usuario ingresa una opción no válida, el sistema debe mostrar un mensaje de error y volver a presentar el menú.
  - El ciclo principal de la aplicación solo finalizará cuando el usuario seleccione la opción "Salir".

-----

### Salida

  - El sistema no produce una salida única, sino que delega la ejecución al módulo seleccionado por el usuario y muestra los resultados correspondientes de dicha operación en la consola.
  - Al seleccionar la opción de salida, muestra un mensaje de despedida.

-----

### Algoritmo

1.  Iniciar el programa.
2.  Mostrar un menú principal con las operaciones disponibles.
3.  Solicitar al usuario que seleccione una opción.
4.  Leer la opción ingresada.
5.  Según la opción, invocar el módulo correspondiente.
6.  Si la opción es "Salir", terminar el programa.
7.  Si la opción no es "Salir", volver al paso 2.

-----

### Refinamiento - Nivel 1

1.  **Inicializar ciclo principal:** Crear un bucle que se ejecute indefinidamente hasta que se indique lo contrario.
2.  **Dentro del bucle:**
    1.  **Mostrar Menú:** Imprimir en consola la lista de módulos disponibles (Consultar Disponibilidad, Registrar Reserva, Confirmar Reserva, Preparar Habitación, Check-in, Check-out, Salir).
    2.  **Capturar Entrada:** Leer el número que el usuario ingrese por teclado.
    3.  **Evaluar Opción:** Utilizar una estructura de control para comparar la entrada del usuario.
    4.  **Ejecutar Módulo:**
          - Si es 1, llamar al Módulo 1.
          - Si es 2, llamar al Módulo 2.
          - ... y así sucesivamente.
          - Si es la opción de salida, romper el bucle.
          - Si no es ninguna opción válida, mostrar un mensaje de error.
3.  **Finalizar programa:** Una vez fuera del bucle, mostrar un mensaje de despedida.

-----

### Refinamiento - Nivel 2

1.  **Bucle principal:** Iniciar un bucle `MIENTRAS VERDADERO`.
2.  **Mostrar Menú en Consola:**
      - Imprimir "--- Sistema de Gestión Hotelera ---".
      - Imprimir "1. Consultar Disponibilidad de Habitaciones".
      - Imprimir "2. Registrar Nueva Reserva".
      - Imprimir "3. Confirmar Reserva (Registrar Pago)".
      - Imprimir "4. Preparar Habitación para Check-in".
      - Imprimir "5. Realizar Check-in".
      - Imprimir "6. Realizar Check-out".
      - Imprimir "7. Salir".
      - Imprimir "Seleccione una opción: ".
3.  **Leer Opción:** Almacenar la entrada del usuario en una variable `opcion`.
4.  **Procesar Opción (estructura condicional):**
      - **Si `opcion` es 1:**
          - Solicitar al usuario las `fechas` y `cantidad_huespedes`.
          - Llamar a la función `MODULO1_CONSULTAR(fechas, cantidad_huespedes)`.
      - **Si `opcion` es 2:**
          - Solicitar al usuario los `datos_huesped`, `habitacion_id`, `fechas`.
          - Llamar a la función `MODULO2_REGISTRAR_RESERVA(...)`.
      - **Si `opcion` es 3:**
          - Solicitar al usuario el `reserva_id` y los `datos_pago`.
          - Llamar a la función `MODULO3_CONFIRMAR_RESERVA(...)`.
      - **Si `opcion` es 4:**
          - Solicitar al usuario el `reserva_id` para identificar la habitación.
          - Llamar a la función `MODULO4_PREPARAR_HABITACION(reserva_id)`.
      - **Si `opcion` es 5:**
          - Solicitar `reserva_id` y `documento_huesped`.
          - Llamar a la función `MODULO5_CHECK_IN(reserva_id, documento_huesped)`.
      - **Si `opcion` es 6:**
          - Solicitar `habitacion_id` y `reserva_id`.
          - Llamar a la función `MODULO6_CHECKOUT(habitacion_id, reserva_id)`.
      - **Si `opcion` es 7:**
          - Imprimir "Gracias por utilizar el sistema. ¡Hasta luego\!".
          - Terminar el bucle.
      - **En otro caso:**
          - Imprimir "Error: Opción no válida. Por favor, intente de nuevo.".
5.  **Pausa Opcional:** Esperar a que el usuario presione una tecla para continuar y limpiar la pantalla antes de volver a mostrar el menú.

-----

### Pseudocódigo

```pseudo
INICIO PROGRAMA_PRINCIPAL
  
  opcion_elegida = 0
  
  MIENTRAS (opcion_elegida != 7) HACER
    
    MOSTRAR "========================================"
    MOSTRAR "   SISTEMA DE GESTIÓN HOTELERA"
    MOSTRAR "========================================"
    MOSTRAR "1. Consultar Disponibilidad"
    MOSTRAR "2. Registrar Reserva"
    MOSTRAR "3. Confirmar Reserva"
    MOSTRAR "4. Preparar Habitación"
    MOSTRAR "5. Realizar Check-in"
    MOSTRAR "6. Realizar Check-out y Liberar Habitación"
    MOSTRAR "7. Salir"
    MOSTRAR "========================================"
    LEER opcion_elegida
    
    SEGUN (opcion_elegida) HACER
      CASO 1:
        MOSTRAR "--- Módulo 1: Consulta de Disponibilidad ---"
        // Aquí se pedirían los datos necesarios para el módulo 1
        // LLAMAR A MODULO1_CONSULTAR()
        
      CASO 2:
        MOSTRAR "--- Módulo 2: Registro de Reserva ---"
        // Aquí se pedirían los datos necesarios para el módulo 2
        // LLAMAR A MODULO2_REGISTRAR_RESERVA()

      CASO 3:
        MOSTRAR "--- Módulo 3: Confirmación de Reserva ---"
        // Aquí se pedirían los datos necesarios para el módulo 3
        // LLAMAR A MODULO3_CONFIRMAR_RESERVA()

      CASO 4:
        MOSTRAR "--- Módulo 4: Preparación de Habitación ---"
        // Aquí se pedirían los datos necesarios para el módulo 4
        // LLAMAR A MODULO4_PREPARAR_HABITACION()

      CASO 5:
        MOSTRAR "--- Módulo 5: Check-in de Huésped ---"
        // Aquí se pedirían los datos necesarios para el módulo 5
        // LLAMAR A MODULO5_CHECK_IN()

      CASO 6:
        MOSTRAR "--- Módulo 6: Check-out y Liberación ---"
        // Aquí se pedirían los datos necesarios para el módulo 6
        // LLAMAR A MODULO6_CHECKOUT()

      CASO 7:
        MOSTRAR "Saliendo del sistema..."
        
      DE OTRO MODO:
        MOSTRAR "Opción no válida. Por favor, ingrese un número del 1 al 7."
        
    FIN SEGUN
    
    // Pausa para que el usuario pueda leer el resultado antes de limpiar la pantalla
    SI (opcion_elegida != 7) ENTONCES
        MOSTRAR "Presione ENTER para continuar..."
        ESPERAR_TECLA()
    FIN SI
    
  FIN MIENTRAS
  
FIN PROGRAMA_PRINCIPAL
```
