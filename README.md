# Turing Machine para Operaciones Aritméticas en Notación Unaria

Este repositorio contiene una implementación en Python de una Máquina de Turing que simula diversas operaciones aritméticas utilizando notación unaria. La idea principal es ilustrar cómo se pueden resolver operaciones matemáticas básicas mediante el concepto de una Máquina de Turing.

## Descripción

La implementación utiliza el concepto de notación unaria (donde cada número se representa mediante una cadena de '1's) y simula las siguientes operaciones mediante máquinas de Turing:

- **Suma**: Realiza la suma de dos números en notación unaria.
- **Resta**: Calcula la resta (no negativa) de dos números en notación unaria.
- **Multiplicación**: Se ofrece una versión directa y otra que simula la multiplicación como suma repetida.
- **División**: Calcula el cociente de una división entera mediante restas repetidas.
- **Potenciación**: Eleva un número a una potencia mediante multiplicaciones sucesivas.
- **Logaritmo Natural Aproximado**: Aproxima el valor del logaritmo natural de un número usando logaritmos en base 2.
- **Función Seno (Simplificada)**: Una implementación simplificada que determina el valor del seno para ángulos específicos en grados.
- **Raíz Cuadrada**: Calcula la raíz cuadrada entera utilizando sumas sucesivas de números impares.

Cada operación se implementa definiendo:
- Una cinta inicial en notación unaria.
- Una tabla de transiciones que define el comportamiento de la máquina.
- La simulación se realiza mostrando paso a paso la cinta, el cabezal y el estado actual.

## Estructura del Código

El código se encuentra organizado en las siguientes secciones:

1. **Utilidades:**  
   Funciones básicas, como `decimal_a_unario(n)`, que convierte un entero a su representación en notación unaria.

2. **Clase TuringMachine:**  
   La implementación central de la máquina de Turing, con métodos para realizar un paso (`step`), ejecutar la máquina (`run`) e imprimir el estado de la cinta (`print_tape`).

3. **Funciones de Operaciones Aritméticas:**  
   Cada operación (suma, resta, multiplicación, división, potenciación, logaritmo, función seno y raíz cuadrada) se implementa en funciones individuales, facilitando la modularidad y el mantenimiento del código.

4. **Función Principal (`main`):**  
   Interactúa con el usuario, solicita los números a operar, ejecuta la máquina de Turing para cada operación y muestra los resultados tanto en notación unaria como en decimal.

## Requisitos

- Python 3.x

## Instrucciones de Uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
