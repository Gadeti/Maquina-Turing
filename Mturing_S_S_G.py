# ------------------------------------------------------------
# Módulo: Turing Machine para Operaciones Aritméticas en Notación Unaria
# Integrantes: Sergio Morales, Gabriela Delgado, Samuel Ramirez
# ------------------------------------------------------------

# -----------------------------
# Sección 1: Utilidades
# -----------------------------
def decimal_a_unario(n):
    """
    Convierte un entero a su representación en notación unaria.
    Ejemplo: 3 -> "111"
    """
    return "1" * n

# -----------------------------
# Sección 2: Clase TuringMachine
# -----------------------------
class TuringMachine:
    def __init__(self, tape, transition_function, initial_state, accept_state, reject_state, blank_symbol='_'):
        """
        Inicializa la máquina de Turing.
        
        Parámetros:
          tape: Cadena inicial de la cinta.
          transition_function: Diccionario con las transiciones {(estado, símbolo): (nuevo_estado, nuevo_símbolo, movimiento)}
          initial_state: Estado inicial.
          accept_state: Estado de aceptación.
          reject_state: Estado de rechazo.
          blank_symbol: Símbolo en blanco.
        """
        self.tape = list(tape)
        self.head = 0
        self.state = initial_state
        self.transition_function = transition_function
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank_symbol = blank_symbol

    def step(self):
        # Lee el símbolo actual o usa el símbolo en blanco si se excede la longitud
        symbol = self.tape[self.head] if self.head < len(self.tape) else self.blank_symbol
        if (self.state, symbol) in self.transition_function:
            new_state, new_symbol, move = self.transition_function[(self.state, symbol)]
            
            # Escribe el nuevo símbolo en la cinta
            if self.head < len(self.tape):
                self.tape[self.head] = new_symbol
            else:
                self.tape.append(new_symbol)
            
            # Mueve el cabezal según la dirección especificada
            if move == 'R':
                self.head += 1
            elif move == 'L':
                self.head -= 1

            # Si el cabezal se mueve fuera del límite izquierdo, se ajusta la cinta
            if self.head < 0:
                self.tape.insert(0, self.blank_symbol)
                self.head = 0

            self.state = new_state
            self.print_tape()  # Muestra el recorrido del cabezal en la cinta
        else:
            self.state = self.reject_state

    def run(self):
        # Ejecuta la máquina hasta llegar a un estado de aceptación o rechazo
        while self.state not in (self.accept_state, self.reject_state):
            self.step()
        return self.state == self.accept_state

    def print_tape(self):
        tape_str = ''.join(self.tape)
        head_marker = ' ' * self.head + '^'
        print("Cinta:", tape_str)
        print("       ", head_marker, f"(Estado: {self.state})\n")

# -----------------------------
# Sección 3: Funciones de Operaciones Aritméticas
# -----------------------------
def addition_unary_machine(a, b):
    """
    Suma dos números representados en notación unaria.
    La cinta tiene la forma: (a en '1's) + "0" + (b en '1's) + "="
    """
    tape = decimal_a_unario(a) + "0" + decimal_a_unario(b) + "="
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '0'): ('q1', '_' , 'R'),
        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', '='): ('qAccept', '_' , 'N'),
    }
    return TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')

def resta(x, y):
    """
    Realiza la resta no negativa en notación unaria (x - y).
    Devuelve el resultado en unario y su longitud (decimal).
    """
    if x < y:
        print("Error: resultado negativo no permitido.")
        return None

    tape = decimal_a_unario(x) + "-" + decimal_a_unario(y) + "="
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '-'): ('q1', '-', 'R'),
        ('q1', '1'): ('q2', 'X', 'L'),
        ('q1', 'X'): ('q1', 'X', 'R'),
        ('q1', '='): ('qAccept', '_' , 'N'),
        ('q2', '1'): ('q2', '1', 'L'),
        ('q2', 'X'): ('q2', 'X', 'L'),
        ('q2', '_'): ('q2', '_', 'L'),
        ('q2', '-'): ('q3', '-', 'L'),
        ('q3', '1'): ('q4', '_' , 'R'),
        ('q3', '_'): ('q3', '_', 'L'),
        ('q4', '1'): ('q4', '1', 'R'),
        ('q4', '_'): ('q4', '_', 'R'),
        ('q4', 'X'): ('q4', 'X', 'R'),
        ('q4', '-'): ('q1', '-', 'R'),
    }
    maquina = TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')
    maquina.run()
    final_tape = ''.join(maquina.tape)
    result_unary = final_tape.split('-')[0].replace('_', '')
    result_decimal = len(result_unary)
    return result_unary, result_decimal

def multiplication_unary(a, b):
    """
    Multiplicación directa en unario (basada en el producto pre-calculado).
    """
    tape = decimal_a_unario(a * b) + "="
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '='): ('qAccept', '=' , 'N')
    }
    maquina = TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')
    maquina.run()
    final_tape = ''.join(maquina.tape)
    result_unary = final_tape.replace("=", "").replace("_", "")
    return result_unary, len(result_unary)

def multiplication_unary_machine(a, b):
    """
    Multiplicación en unario simulada como suma repetida usando una máquina de Turing.
    """
    if b == 0:
        return "", 0

    resultado = decimal_a_unario(a)
    for _ in range(b - 1):
        tape = resultado + "0" + decimal_a_unario(a) + "="
        transitions = {
            ('q0', '1'): ('q0', '1', 'R'),
            ('q0', '0'): ('q1', '0', 'R'),
            ('q1', '1'): ('q2', '_', 'N'),
            ('q1', '='): ('q3', '=', 'N'),
            ('q2', '1'): ('q2', '1', 'L'),
            ('q2', '0'): ('q2', '0', 'L'),
            ('q2', '_'): ('q0', '1', 'R'),
            ('q3', '1'): ('q3', '1', 'R'),
            ('q3', '='): ('qAccept', '=', 'N'),
        }
        maquina = TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')
        maquina.run()
        final_tape = ''.join(maquina.tape)
        # Se remueven los separadores y símbolos innecesarios
        resultado = final_tape.replace("0", "").replace("=", "").replace("_", "")
    return resultado, len(resultado)

def power_unary(x, y):
    """
    Calcula x^y mediante multiplicación repetida.
    """
    if y == 0:
        return "1", 1
    result_unary = decimal_a_unario(x)
    for _ in range(y - 1):
        current_value = len(result_unary)
        result_unary, _ = multiplication_unary(current_value, x)
    return result_unary, len(result_unary)

def log_unary(x):
    """
    Aproxima ln(x) de forma indirecta:
      1. Calcula floor(log₂(x)) mediante divisiones enteras.
      2. Aproxima ln(x) como floor(log₂(x) * ln(2)), con ln(2) ≈ 0.693.
      
    Retorna:
      - La representación en unario de floor(log₂(x)).
      - El valor entero de floor(log₂(x)).
      - La aproximación entera de ln(x).
    """
    if x < 1:
        return "", 0, 0
    iterations = 0
    n = x
    while n >= 2:
        n = n // 2
        iterations += 1
    iterations_unary = decimal_a_unario(iterations)
    ln_approx = int(iterations * 0.693)
    return iterations_unary, iterations, ln_approx

def sin_unary(angle):
    """
    Función seno simplificada en unario.
    La máquina se basa en la entrada del ángulo y retorna 1 si es múltiplo de 90° (con un comportamiento
    especial para 90° o 270°) o 0 en otro caso.
    """
    tape = decimal_a_unario(int(angle)) + "s" + "="
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', 's'): ('qAccept', 's', 'N'),
        ('q0', '='): ('qAccept', '=', 'N'),
    }
    maquina = TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')
    maquina.run()
    # Retorna la máquina y 1 si el ángulo (en grados) es múltiplo de 90 (ajustado a un comportamiento simplificado)
    return maquina, 1 if int(angle) % 180 == 90 else 0

def sqrt_turing_machine():
    """
    Calcula la raíz cuadrada entera de un número usando sumas sucesivas de impares.
    Imprime el resultado en notación unaria y en decimal.
    """
    number = int(input("Ingresa un número para calcular su raíz cuadrada: "))
    count = 0
    odd = 1  # Primer número impar

    while number >= odd:
        number -= odd
        count += 1
        odd += 2  # Siguiente número impar

    tape = decimal_a_unario(count) + "="
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '='): ('qAccept', '=', 'N'),
    }
    maquina = TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')
    maquina.run()

    print("Raíz cuadrada en unario:", ''.join(maquina.tape).replace("=", ""))
    print("Raíz cuadrada en decimal:", count)

def division_unary(a, b):
    """
    Calcula el cociente de a // b en notación unaria mediante restas repetidas.
    
    Parámetros:
      a: Dividendo (entero positivo).
      b: Divisor (entero positivo, distinto de 0).
    
    Retorna:
      - El cociente en notación unaria.
      - Su valor decimal (longitud de la cadena unaria).
    """
    if b == 0:
        print("Error: División por cero.")
        return None, None

    dividend = a
    quotient = ""
    while dividend >= b:
        resta_result = resta(dividend, b)
        if resta_result is None:
            break
        _, new_dividend = resta_result
        dividend = new_dividend
        quotient += "1"
    return quotient, len(quotient)

# -----------------------------
# Sección 4: Función Principal con Menú
# -----------------------------
def main():
    while True:
        print("\n=== Máquina de Turing para Operaciones Aritméticas en Notación Unaria ===")
        print("Seleccione la operación a realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación (suma repetida)")
        print("4. División")
        print("5. Potenciación")
        print("6. Aproximación del Logaritmo Natural (ln)")
        print("7. Función Seno (simplificada)")
        print("8. Raíz Cuadrada")
        print("9. Salir")
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion == '9':
            print("Saliendo del programa.")
            break
        
        if opcion == '1':
            print("\n>> Suma en Notación Unaria:")
            a = int(input("Ingrese el primer número (entero positivo): "))
            b = int(input("Ingrese el segundo número (entero positivo): "))
            maquina = addition_unary_machine(a, b)
            if maquina.run():
                final_tape = ''.join(maquina.tape)
                result_unary = final_tape.replace("_", "")
                result_decimal = len(result_unary)
                print("Resultado en notación unaria:", result_unary)
                print("Resultado en decimal:", result_decimal)
            else:
                print("La máquina rechazó la entrada.")
        
        elif opcion == '2':
            print("\n>> Resta en Notación Unaria:")
            x = int(input("Ingrese el minuendo (entero positivo): "))
            y = int(input("Ingrese el sustraendo (entero positivo): "))
            resultado = resta(x, y)
            if resultado:
                result_unary, result_decimal = resultado
                print("Resultado en notación unaria:", result_unary)
                print("Resultado en decimal:", result_decimal)
        
        elif opcion == '3':
            print("\n>> Multiplicación en Notación Unaria (suma repetida):")
            a = int(input("Ingrese el primer número (entero positivo): "))
            b = int(input("Ingrese el segundo número (entero positivo): "))
            result_unary, result_decimal = multiplication_unary_machine(a, b)
            print("Resultado en notación unaria:", result_unary)
            print("Resultado en decimal:", result_decimal)
        
        elif opcion == '4':
            print("\n>> División en Notación Unaria:")
            a = int(input("Ingrese el numerador (entero positivo): "))
            b = int(input("Ingrese el denominador (entero positivo distinto de 0): "))
            if a < 1 or b < 1:
                print("Solo se permiten números enteros positivos.")
            else:
                q_unario, q_decimal = division_unary(a, b)
                if q_unario is not None:
                    print("Cociente en notación unaria:", q_unario)
                    print("Cociente en decimal:", q_decimal)
        
        elif opcion == '5':
            print("\n>> Potenciación en Notación Unaria:")
            base = int(input("Ingrese la base (entero positivo): "))
            exp = int(input("Ingrese el exponente (entero no negativo): "))
            result_unary, result_decimal = power_unary(base, exp)
            print("Resultado en notación unaria:", result_unary)
            print("Resultado en decimal:", result_decimal)
        
        elif opcion == '6':
            print("\n>> Aproximación del Logaritmo Natural (ln) en Notación Unaria:")
            x_val = int(input("Ingrese un número (entero positivo mayor o igual a 1): "))
            log_unario, log_val, ln_approx = log_unary(x_val)
            print("Representación unaria de floor(log₂(x)):", log_unario, "-> valor =", log_val)
            print("Aproximación entera de ln(x):", ln_approx)
        
        elif opcion == '7':
            print("\n>> Función Seno en Notación Unaria (versión simplificada):")
            angle = float(input("Ingrese un ángulo en grados (número positivo): "))
            maquina_sin, sin_value = sin_unary(angle)
            final_tape = ''.join(maquina_sin.tape)
            print("Cinta final:", final_tape)
            print("Valor de sin(angle):", sin_value)
        
        elif opcion == '8':
            print("\n>> Raíz Cuadrada (cálculo mediante sumas de impares):")
            sqrt_turing_machine()
        
        else:
            print("Opción no válida. Intente nuevamente.")
        
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()

