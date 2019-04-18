from random import randrange

class Rsa(object):
    """docstring for RSA."""
    '''def __init__(self, message, p, q, n):
        super(RSA, self).__init__()'''

    def euclids_algorithm(a, b):
        rest = 1
        while b != 0:
            rest = a % b
            a = b
            b = rest
        return a

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
            if(Rsa.is_prime(x) == True):
                return x

    def setup(check):
        if check == 1:
            while True:
                p = Rsa.generate_prime()
                q = Rsa.generate_prime()

                if p > q:
                    break
        else:
            while True:
                p = int(input('Digite p: '))
                q = int(input('Digite q: '))
                if Rsa.is_prime(p) == False or Rsa.is_prime(q) == False:
                    print('Erro! O número digitado não é primo.')
                else:
                    if p > q:
                        break

        n = p * q
        phi = (p-1) * (q-1)

        # Generate e |1 < e < phi and coprime
        while True:
            e = randrange(1 , phi)
            if (Rsa.euclids_algorithm(e, phi) == 1):
                break

        # Generate private key
        pk=0
        while ((pk*e) % phi)!= 1:
            pk = pk + 1

        print("Sua chave pública é: (%d, %d)" % (n, e))

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

        encrypted = "".join(str(encrypted_message))

        f_encrypted_message = open('encrypted_message.txt', 'w')
        f_encrypted_message.write(str(encrypted))
        f_encrypted_message.close()

        print('Menssagem criptografada está salva no arquivo encrypted_message.txt\n')
        return encrypted

    def decrypt(encry_message, block_size = 2):
        f_open = open('private_keys.txt', 'r')
        n = int(f_open.readline())
        pk = int(f_open.readline())
        f_open.close

        list_blocks = encry_message.split(',')
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