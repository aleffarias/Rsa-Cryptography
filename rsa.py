from random import randrange

class Rsa(object):
    """docstring for RSA."""
    '''def __init__(self, message, p, q, n):
        super(RSA, self).__init__()

        self.message = message
        self.p = None
        self.q = None
        self.n = Nome'''

    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for n in range(3, int(num**0.5)+2, 2):
            if num % n == 0:
                return False
        return True

    def generate_prime():
        while True:
            x = randrange(1,1000)
            if(Rsa.is_prime(x) == True):
                return x

    def setup():
        while True:
            p = Rsa.generate_prime()
            q = Rsa.generate_prime()

            if p != q:
                break
        n = p * q
        phi = (p-1) * (q-1)
        e = randrange(2 , phi)


    '''def totiente():

    def encrypt():

    def decrypt():'''

Rsa.setup()