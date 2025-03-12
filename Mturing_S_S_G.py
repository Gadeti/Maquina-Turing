#Integrantes:   Sergio Morales
#               Gabriela Delgado
#               Samuel Ramirez


# ---------------------------------------------------------------------
# Función para convertir un número entero a notación unaria (cadena de '1's)
# ---------------------------------------------------------------------
def decimal_a_unario(n):
    return "1" * n

# ---------------------------------------------------------------------
# Clase TuringMachine: Simulación de una Máquina de Turing general
# ---------------------------------------------------------------------
class TuringMachine:
    def __init__(self, tape, transition_function, initial_state, accept_state, reject_state, blank_symbol='_'):
        self.tape = list(tape)            # La cinta se representa como una lista de símbolos.
        self.head = 0                     # Posición inicial del cabezal.
        self.state = initial_state        # Estado inicial.
        self.transition_function = transition_function  # Tabla de transiciones.
        self.accept_state = accept_state  # Estado de aceptación.
        self.reject_state = reject_state  # Estado de rechazo.
        self.blank_symbol = blank_symbol  # Símbolo en blanco.

    def step(self):
        symbol = self.tape[self.head] if self.head < len(self.tape) else self.blank_symbol
        if (self.state, symbol) in self.transition_function:
            new_state, new_symbol, move = self.transition_function[(self.state, symbol)]
            
            if self.head < len(self.tape):
                self.tape[self.head] = new_symbol
            else:
                self.tape.append(new_symbol)

            if move == 'R':
                self.head += 1
            elif move == 'L':
                self.head -= 1

            if self.head < 0:
                self.tape.insert(0, self.blank_symbol)
                self.head = 0

            self.state = new_state
            self.print_tape()
        else:
            self.state = self.reject_state

    def run(self):
        while self.state not in (self.accept_state, self.reject_state):
            self.step()
        return self.state == self.accept_state

    def print_tape(self):
        tape_str = ''.join(self.tape)
        head_marker = ' ' * self.head + '^'
        print("Cinta:", tape_str)
        print("       ", head_marker, f"(Estado: {self.state})")
        print()

# ---------------------------------------------------------------------
# Máquina de Turing para la suma en notación unaria (método sencillo)
# ---------------------------------------------------------------------
def addition_unary_machine(a, b):
    tape = decimal_a_unario(a) + "0" + decimal_a_unario(b) + "="
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '0'): ('q1', '_' , 'R'),
        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', '='): ('qAccept', '_' , 'N'),
    }
    return TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')

# ---------------------------------------------------------------------
# Máquina de Turing para la resta en notación unaria (resta no negativa)
# ---------------------------------------------------------------------
def resta(x, y):
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

# ---------------------------------------------------------------------
# Máquina de Turing para la multiplicación en notación unaria
# ---------------------------------------------------------------------
def multiplication_unary(a, b):
    tape = decimal_a_unario(a * b) + "="
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '='): ('qAccept', '=' , 'N')
    }
    machine = TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')
    machine.run()
    final_tape = ''.join(machine.tape)
    result_unary = final_tape.replace("=", "").replace("_", "")
    return result_unary, len(result_unary)

# ---------------------------------------------------------------------
# Máquina de Turing para la potenciación en notación unaria
# (Calcula x^y mediante multiplicación repetida usando multiplication_unary)
# ---------------------------------------------------------------------
def power_unary(x, y):
    if y == 0:
        return "1", 1
    result_unary = decimal_a_unario(x)
    for _ in range(y - 1):
        current_value = len(result_unary)
        result_unary, _ = multiplication_unary(current_value, x)
    return result_unary, len(result_unary)

# ---------------------------------------------------------------------
# Aproximación del logaritmo natural (ln) usando log₂(x)
# ---------------------------------------------------------------------
def log_unary(x):
    """
    Aproxima ln(x) (parte entera) de forma indirecta:
      1. Calcula floor(log₂(x)) usando divisiones enteras (empleando Python).
      2. Luego usa la relación ln(x) ≈ floor(log₂(x) * ln(2)), con ln(2) ≈ 0.693.
    Se devuelve:
      - La representación unaria de floor(log₂(x)).
      - floor(log₂(x)) (valor entero).
      - Aproximación entera de ln(x).
    """
    if x < 1:
        return "", 0, 0
    iterations = 0
    n = x
    while n >= 2:
        n = n // 2
        iterations += 1
    iterations_unary = "1" * iterations
    ln_approx = int(iterations * 0.693)
    return iterations_unary, iterations, ln_approx

def sin_unary(angle):

    tape = decimal_a_unario(int(angle)) + "s" + "="
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', 's'): ('qAccept', 's', 'N'),
        ('q0', '='): ('qAccept', '=', 'N'),
    }
    machine = TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')
    machine.run()
    
    # Se devuelve 1 si el ángulo es múltiplo de 90°
    return machine, 1 if int(angle) % 180 == 90 else 0

def sqrt_turing_machine():
    """
    Calcula la raíz cuadrada entera de un número usando sumas sucesivas de impares.
    Se representa en notación unaria y decimal.
    """
    number = int(input("Ingresa un número para calcular su raíz cuadrada: "))
    count = 0
    odd = 1  # Primer número impar
    
    while number >= odd:
        number -= odd
        count += 1
        odd += 2  # Siguiente impar

    # Representación en unario
    tape = decimal_a_unario(count) + "="
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '='): ('qAccept', '=', 'N'),
    }
    machine = TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')
    machine.run()

    # Imprime resultados
    print("Raíz cuadrada en unario:", ''.join(machine.tape).replace("=", ""))
    print("Raíz cuadrada en decimal:", count)

def multiplication_unary_machine(a, b):
    """
    Máquina de Turing para la multiplicación en notación unaria.
    La multiplicación se realiza como sumas repetidas usando la máquina de Turing de suma.
    """
    if b == 0:
        return "", 0
    
    resultado = decimal_a_unario(a)

    for _ in range(b - 1):  # Se repite la suma (b-1) veces
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
        machine = TuringMachine(tape, transitions, 'q0', 'qAccept', 'qReject', blank_symbol='_')
        machine.run()
        final_tape = ''.join(machine.tape)
        resultado = final_tape.replace("0", "").replace("=", "").replace("_", "")

    return resultado, len(resultado)

#_____________________________________________________________________________

def division_unary(a, b):
    """
    Calcula el cociente de a // b en notación unaria mediante resta repetida.
    
    Parámetros:
      a: Dividendo (entero positivo).
      b: Divisor (entero positivo distinto de 0).

    Retorna:
      - El cociente en notación unaria.
      - Su longitud (el resultado en decimal).
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

        result_unary, new_dividend = resta_result  # Obtener el nuevo dividendo
        dividend = new_dividend
        quotient += "1"  # Cada resta representa una unidad en el cociente

    return quotient, len(quotient)




# ---------------------------------------------------------------------
# Main: Ejecución de las operaciones
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Operaciones en notación unaria utilizando Máquina de Turing ===")

    # Prueba de la suma
    print("\nMáquina de Turing para Suma en notación unaria:")
    a = int(input("Ingrese el primer número (entero positivo): "))
    b = int(input("Ingrese el segundo número (entero positivo): "))
    machine = addition_unary_machine(a, b)
    accepted = machine.run()
    final_tape = ''.join(machine.tape)
    result_unary = final_tape.replace("_", "")
    result_decimal = len(result_unary)
    if accepted:
        print("Cinta final:", final_tape)
        print("Resultado en notación unaria:", result_unary)
        print("Resultado en decimal:", result_decimal)
    else:
        print("La máquina rechazó la entrada.")

    # Prueba de la resta
    print("\nMáquina de Turing para Resta en notación unaria:")
    x = int(input("Ingrese el minuendo (entero positivo): "))
    y = int(input("Ingrese el sustraendo (entero positivo): "))
    resta_result = resta(x, y)
    if resta_result is not None:
        result_unary, result_decimal = resta_result
        print("Resultado en notación unaria:", result_unary)
        print("Resultado en decimal:", result_decimal)

    # Prueba de la multiplicación
    print("\nMáquina de Turing para Multiplicación en notación unaria:")
    a = int(input("Ingrese el primer número (entero positivo): "))
    b = int(input("Ingrese el segundo número (entero positivo): "))
    unary_result, decimal_result = multiplication_unary_machine(a, b)
    print(f"Resultado en notación unaria: {unary_result}")
    print(f"Resultado en decimal: {decimal_result}")

    # Prueba de la división
    print("\nMáquina de Turing para División en notación unaria:")
    try:
        a = int(input("Ingrese el numerador (entero positivo): "))
        b = int(input("Ingrese el denominador (entero positivo distinto de 0): "))

        if a < 1 or b < 1:
            print("Solo se permiten números enteros positivos.")
        else:
            q, q_len = division_unary(a, b)
            if q is not None:
                print("Cociente en notación unaria:", q)
                print("Cociente en decimal:", q_len)
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")

    # Prueba de la potenciación
    print("\nMáquina de Turing para Potenciación en notación unaria:")
    base = int(input("Ingrese la base (entero positivo): "))
    exp = int(input("Ingrese el exponente (entero no negativo): "))
    power_result, power_decimal = power_unary(base, exp)
    print("Resultado en notación unaria:", power_result)
    print("Resultado en decimal:", power_decimal)

    # Prueba de la función log_unary (aproximación de ln(x))
    print("\nAproximación del Logaritmo Natural (ln) en notación unaria:")
    x_val = int(input("Ingrese un número (entero positivo mayor o igual a 1): "))
    log2_unario, log2_value, ln_approx = log_unary(x_val)
    print("Representación unaria de floor(log₂(x)):", log2_unario, "-> valor =", log2_value)
    print("Aproximación entera de ln(x):", ln_approx)

    # Prueba de la función sin_unary
    print("\nMáquina de Turing para la Función Seno en notación unaria (versión simplificada):")
    angle = float(input("Ingrese un ángulo en grados (número positivo): "))
    sin_machine, sin_value = sin_unary(angle)
    final_tape = ''.join(sin_machine.tape)
    print("Cinta final:", final_tape)
    print("Valor de sin(angle):", sin_value)

    # Prueba de la función raíz cuadrada
    print("\nMáquina de Turing para la Raíz Cuadrada:")
    sqrt_turing_machine()
