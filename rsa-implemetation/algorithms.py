from random import randrange

class Algorithms(object):
    """docstring for ."""

    def euclids_algorithm(a, b):
        rest = 1
        while b != 0:
            rest = a % b
            a = b
            b = rest
        return a

    def extended_euclids_algorithm(a, b):
        x, old_x = 0, 1
        y, old_y = 1, 0

        while (b != 0):
            quotient = a // b
            a, b = b, a - quotient * b
            old_x, x = x, old_x - quotient * x
            old_y, y = y, old_y - quotient * y

        return a, old_x, old_y

    def is_prime(num):
        if num == 2:
            return True

        if (num < 2) or (num % 2) == 0:
            return False

        for n in range(3, int(num**0.5)+2, 2):
            if num % n == 0:
                return False
        return True

    def generate_prime():
        while True:
            x = randrange(1,100)
            if(Algorithms.is_prime(x) == True):
                return x