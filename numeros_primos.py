# New chat detected.. initialising new project mode 🥷👾💻

def solicitar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero mayor que 1: "))
            if numero > 1:
                return numero
            else:
                print("El número debe ser mayor que 1. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def factorizar(numero):
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return factores

def main():
    numero = solicitar_numero()
    factores_primos = factorizar(numero)
    print(f"Factores primos de {numero}: {factores_primos}")

if __name__ == "__main__":
    main()
