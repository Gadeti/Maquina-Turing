A continuación se muestra un ejemplo de un archivo README.md detallado para el código proporcionado:

---

# Máquina de Turing para Operaciones Aritméticas en Notación Unaria

Este proyecto implementa una **Máquina de Turing** en Python para realizar diversas operaciones aritméticas usando notación unaria. La implementación está dividida en módulos que incluyen utilidades, la definición de la máquina de Turing y funciones para cada operación aritmética. El código fue desarrollado por **Sergio Morales**, **Gabriela Delgado** y **Samuel Ramirez**.

---

## Índice

- [Descripción General](#descripción-general)
- [Estructura del Código](#estructura-del-código)
  - [Utilidades](#utilidades)
  - [Clase TuringMachine](#clase-turingmachine)
  - [Funciones de Operaciones Aritméticas](#funciones-de-operaciones-aritméticas)
  - [Función Principal](#función-principal)
- [Operaciones Implementadas](#operaciones-implementadas)
  - [Suma](#suma)
  - [Resta](#resta)
  - [Multiplicación](#multiplicación)
  - [Multiplicación (suma repetida)](#multiplicación-suma-repetida)
  - [Potenciación](#potenciación)
  - [Logaritmo Natural Aproximado](#logaritmo-natural-aproximado)
  - [Función Seno Simplificada](#función-seno-simplificada)
  - [Raíz Cuadrada](#raíz-cuadrada)
  - [División](#división)
- [Ejecución](#ejecución)
- [Consideraciones y Límites](#consideraciones-y-límites)
- [Licencia](#licencia)

---

## Descripción General

El proyecto simula una Máquina de Turing para realizar operaciones aritméticas en notación unaria. En esta representación, un número entero se representa mediante una secuencia de caracteres "1". Por ejemplo, el número 3 se representa como `"111"`. Cada operación aritmética se resuelve manipulando la cinta de la máquina a través de funciones de transición definidas en un diccionario.

La máquina acepta o rechaza la entrada en función de los estados definidos y se desplaza a lo largo de la cinta para leer y escribir símbolos, permitiendo la simulación de operaciones como suma, resta, multiplicación, división, potenciación, cálculo aproximado de logaritmos, función seno simplificada y raíz cuadrada.

---

## Estructura del Código

### Utilidades

- **`decimal_a_unario(n)`**:  
  Convierte un entero `n` a su representación en notación unaria.  
  **Ejemplo:** `3` → `"111"`.

### Clase TuringMachine

- **Constructor (_init_)**:  
  Inicializa la máquina de Turing recibiendo:
  - `tape`: La cadena que representa la cinta.
  - `transition_function`: Un diccionario que define las transiciones de la máquina en el formato `{(estado, símbolo): (nuevo_estado, nuevo_símbolo, movimiento)}`.
  - `initial_state`: Estado inicial.
  - `accept_state`: Estado de aceptación.
  - `reject_state`: Estado de rechazo.
  - `blank_symbol`: Símbolo que representa el espacio en blanco (por defecto es una cadena vacía o se redefine como `_`).

- **Métodos Principales:**
  - `step()`: Realiza un solo paso de la máquina de Turing, leyendo el símbolo actual, aplicando la transición correspondiente y moviendo el cabezal.
  - `run()`: Ejecuta la máquina de Turing hasta alcanzar el estado de aceptación o rechazo.
  - `print_tape()`: Imprime el contenido actual de la cinta junto con la posición del cabezal y el estado actual de la máquina.

### Funciones de Operaciones Aritméticas

Cada función implementa una operación aritmética mediante la simulación de una Máquina de Turing:

- **Suma (`addition_unary_machine`)**:  
  Suma dos números en notación unaria. La cinta se construye con los operandos separados por un `"0"` y finalizada con `"="`. Se define un conjunto de transiciones para mover el cabezal y escribir los símbolos necesarios, validando la operación.

- **Resta (`resta`)**:  
  Realiza la resta no negativa (x - y) en notación unaria. Valida que el minuendo sea mayor o igual que el sustraendo, utilizando una serie de transiciones para marcar y restar unidades.

- **Multiplicación (`multiplication_unary`)**:  
  Implementa la multiplicación directa en unario, basado en el producto pre-calculado, y actualiza la cinta para reflejar el resultado.

- **Multiplicación por Suma Repetida (`multiplication_unary_machine`)**:  
  Simula la multiplicación mediante la suma repetida de números. Se itera construyendo una cinta con el acumulado de la suma hasta llegar al resultado.

- **Potenciación (`power_unary`)**:  
  Calcula la potencia (x^y) utilizando la multiplicación repetida. Se parte del valor base y se multiplica en cada iteración.

- **Logaritmo Natural Aproximado (`log_unary`)**:  
  Aproxima el logaritmo natural de un número. Primero, calcula el floor del logaritmo base 2 a través de divisiones enteras y luego utiliza la aproximación `ln(2) ≈ 0.693` para obtener un valor aproximado.

- **Función Seno Simplificada (`sin_unary`)**:  
  Implementa una versión simplificada de la función seno en notación unaria. La máquina retorna 1 si el ángulo es múltiplo de 90° (especialmente para 90° o 270°) y 0 en otros casos.

- **Raíz Cuadrada (`sqrt_turing_machine`)**:  
  Calcula la raíz cuadrada entera de un número usando la suma sucesiva de números impares. La función imprime el resultado tanto en notación unaria como en su representación decimal.

- **División (`division_unary`)**:  
  Calcula el cociente de la división entera (a // b) en notación unaria mediante restas repetidas. Valida que el divisor sea mayor a cero y construye el resultado acumulando las restas.

### Función Principal

- **`main()`**:  
  Función que integra la ejecución de todas las operaciones. Solicita al usuario ingresar los valores para cada operación, ejecuta la máquina de Turing correspondiente y muestra el resultado en notación unaria y en decimal.

---

## Operaciones Implementadas

### Suma

- **Descripción:**  
  Suma dos números representados en notación unaria. La cinta se organiza con los operandos separados por un separador `"0"` y se finaliza con `"="`.

- **Funcionamiento:**  
  La máquina recorre los dígitos del primer operando, detecta el separador, y luego procede a concatenar los dígitos del segundo operando.

### Resta

- **Descripción:**  
  Realiza la resta no negativa (x - y) en notación unaria.  
  **Nota:** Se controla que el resultado no sea negativo.

- **Funcionamiento:**  
  La máquina utiliza transiciones que marcan y eliminan los dígitos correspondientes a la resta y retorna el resultado en forma unaria y su longitud (valor decimal).

### Multiplicación

- **Multiplicación Directa:**  
  Se construye la cinta con el producto pre-calculado en notación unaria.  
- **Multiplicación por Suma Repetida:**  
  Se simula la multiplicación sumando repetidamente el primer número la cantidad de veces indicada por el segundo número.

### Potenciación

- **Descripción:**  
  Calcula la potencia (x^y) mediante la multiplicación repetida de la base.

- **Funcionamiento:**  
  Se parte del valor base en notación unaria y se multiplica en cada iteración utilizando la función de multiplicación directa.

### Logaritmo Natural Aproximado

- **Descripción:**  
  Aproxima el logaritmo natural de un número a partir del cálculo del floor de log₂(x).  
- **Funcionamiento:**  
  Realiza divisiones enteras hasta que el número sea menor que 2 para contar las iteraciones (que representan el floor del logaritmo base 2) y utiliza la constante `0.693` para obtener una aproximación de ln(x).

### Función Seno Simplificada

- **Descripción:**  
  Calcula de forma simplificada el valor de la función seno para un ángulo dado, retornando 1 para ciertos ángulos (múltiplos de 90° con un caso especial) y 0 en otros casos.

### Raíz Cuadrada

- **Descripción:**  
  Calcula la raíz cuadrada entera de un número mediante la suma de números impares consecutivos.

- **Funcionamiento:**  
  Se resta el siguiente número impar del valor original hasta que el residuo sea menor que el siguiente impar; el número de iteraciones representa la raíz cuadrada entera.

### División

- **Descripción:**  
  Calcula el cociente de la división entera (a // b) usando restas repetidas.

- **Funcionamiento:**  
  Se realiza una resta de `b` sobre `a` de forma iterativa hasta que `a` sea menor que `b`, acumulando en la variable `quotient` cada resta exitosa.

---

## Ejecución

Para ejecutar el programa, se debe llamar a la función principal `main()`, que se encarga de:

1. Solicitar al usuario los operandos para cada operación.
2. Ejecutar la máquina de Turing correspondiente para la operación.
3. Imprimir el resultado en notación unaria y su equivalente decimal.

**Nota:**  
El bloque final utiliza la condición `if _name_ == "_main_":` para garantizar que la función `main()` se ejecute cuando el script sea ejecutado directamente.

---

## Consideraciones y Límites

- **Notación Unaria:**  
  La representación de números en notación unaria resulta poco eficiente para números grandes, ya que el tamaño de la cinta crece linealmente con el valor del número.

- **Máquina de Turing:**  
  La simulación se basa en transiciones definidas manualmente. Cualquier cambio en las operaciones o en la estructura de la cinta requerirá ajustar las funciones de transición.

- **Errores y Validaciones:**  
  Algunas funciones validan las entradas (por ejemplo, la resta no permite resultados negativos y la división controla el divisor cero). Sin embargo, se recomienda validar cuidadosamente los datos de entrada para evitar errores durante la ejecución.

- **Limitaciones del Modelo:**  
  La implementación de algunas operaciones (como la función seno) es simplificada y no refleja completamente el comportamiento matemático esperado para todos los ángulos.

---

## Licencia

Este proyecto se distribuye bajo [inserte aquí la licencia correspondiente] y fue desarrollado para fines educativos y de demostración en el uso de Máquinas de Turing para operaciones aritméticas en notación unaria.

---

Este README.md proporciona una guía completa sobre la estructura y funcionamiento del código, permitiendo a los usuarios y desarrolladores entender y extender la implementación de la Máquina de Turing para operaciones aritméticas en notación unaria.


