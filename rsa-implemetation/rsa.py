from random import randrange
from algorithms import Algorithms

class Rsa(object):
    """docstring for RSA."""
    '''def __init__(self, message, p, q, n):
        super(RSA, self).__init__()'''

    def setup(check):
        # Generate key automatically
        if check == 1:

            p = Algorithms.generate_prime()
            q = Algorithms.generate_prime()

            print("P: %d\nQ: %d" % (p, q))

            n = p * q
            phi = (p-1) * (q-1)

            # Generate e |1 < e < phi and coprime
            while True:
                e = randrange(1 , phi)
                if (Algorithms.euclids_algorithm(e, phi) == 1):
                    break

            # Generate private key
            gcd, x, y = Algorithms.extended_euclids_algorithm(e, phi)

            # make sure d is positive
            if (x < 0):
                pk = x + phi
            else:
                pk = x

            print("\nSua chave pública (n, e) é: (%d, %d)" % (n, e))

            # Write the public keys n and e to a file
            public_k = open('public_keys.txt', 'w')
            public_k.write(str(n) + '\n')
            public_k.write(str(e))
            public_k.close()

            # Write the private key
            private_k = open('private_keys.txt', 'w')
            private_k.write(str(n) + '\n')
            private_k.write(str(pk))
            private_k.close()
        else:
            # User adds keys
            print('\nDigite a chave pública!')
            n = int(input('  Digite n (p * q): '))
            e = int(input('  Digite e (1 < e < phi): '))

            print('\nDigite a chave privada!')
            pk = int(input('\tDigite a chave privada (d): '))

            print("\nSua chave pública (n, e) é: (%d, %d)" % (n, e))

            # Write the public keys n and e to a file
            public_k = open('public_keys.txt', 'w')
            public_k.write(str(n) + '\n')
            public_k.write(str(e))
            public_k.close()

            # Write the private key
            private_k = open('private_keys.txt', 'w')
            private_k.write(str(n) + '\n')
            private_k.write(str(pk))
            private_k.close()


    def encrypt(message, file = 'public_keys.txt'):
        try:
            f_open = open(file, 'r')

        except FileNotFoundError:
            print('Arquivo não encontrado.')
        else:
            n = int(f_open.readline())
            e = int(f_open.readline())
            f_open.close()

        encrypted_message = []

        for i in range(0, len(message)):
            cipher = ord(message[i])
            encrypted_message.append((cipher ** e) % n)

        #encrypted = " ".join(str(encrypted_message))
        #encrypted = str(encrypted_message).strip('[]')
        encrypted = " ".join(map(str, encrypted_message))

        f_encrypted_message = open('encrypted_message.txt', 'w')
        f_encrypted_message.write(encrypted)
        f_encrypted_message.close()

        print('Menssagem criptografada está salva no arquivo encrypted_message.txt')
        return encrypted

    def decrypt(n, pk, encry_message, block_size = 2):
        if (n and pk) == 0:
            f_open = open('private_keys.txt', 'r')
            n = int(f_open.readline())
            pk = int(f_open.readline())
            f_open.close

        list_blocks = encry_message.split(' ')
        int_blocks = []

        for s in list_blocks:
            int_blocks.append(int(s))

        message = ""

        for i in range(len(int_blocks)):
            int_blocks[i] = (int_blocks[i]**pk) % n

            tmp = ""
            for c in range(block_size):
                tmp = chr(int_blocks[i] % 1000) + tmp
                int_blocks[i] //= 1000
            message += tmp

        return message