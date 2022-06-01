import sys


if len(sys.argv) < 3:
    print("te falto poner un numero")
    sys.exit(1)

try:
    numero_1 = int(sys.argv[1])
    numero_2 = int(sys.argv[2])
except:
    print("lo ingresado no es un numero")
    sys.exit(1)


def numeros_amigos(inicio, fin):
    """
    It takes a range of numbers and prints out the pairs
    of amicable numbers within that range

    :param inicio: the starting number
    :param fin: the number you want to stop at
    """

    for numero in range(inicio, fin):

        numero_1 = numero

        # Finding the sum of the divisors of the number 1.
        contador_1 = 0
        divisores_1 = []
        for divisor in range(1, numero_1):

            if numero_1 % divisor == 0:
                divisores_1.append(divisor)
                contador_1 += 1
        suma_divisores_1 = sum(divisores_1)

        numero_2 = suma_divisores_1

        # Finding the sum of the divisors of the number 2.
        contador_2 = 0
        divisores_2 = []
        for divisor in range(1, numero_2):

            if numero_2 % divisor == 0:
                divisores_2.append(divisor)
                contador_2 += 1
        suma_divisores_2 = sum(divisores_2)

        # Checking if the sum of the divisors of the second number is
        # equal to the first number. If it is,
        # it checks if the first number
        # is not equal to the second number.
        # If it is not, it checks
        # if the first number is less than the second number.
        # If it is, it prints out the pair of
        # numbers.
        if suma_divisores_2 == numero:
            if numero != numero_2:
                if numero < numero_2:
                    print(numero, numero_2)


numeros_amigos(numero_1, numero_2)
