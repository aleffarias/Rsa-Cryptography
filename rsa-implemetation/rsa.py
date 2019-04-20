from random import randrange
from algorithms import Algorithms

class Rsa(object):
    """Funções para ."""
    '''def __init__(self, message, p, q, n):
        super(RSA, self).__init__()'''

    def setup(check):
        """
        Cria as chaves pública e privada respeitando as restrições do algoritmo de criptografia RSA.
        As chaves são escritas nos arquvios public_keys.txt e private_keys.txt.

        Args:
            check (int): verifica se as chaves seram geradas automaticamente
                        ou fornecidas pelo usuário.
        """
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
        """
            Recebe uma string para ser criptografada com as chaves geradas ou fornecidas pelo usuário.
            Com cada caracter da string (valor ASCII) é feita a operação de pontecia com o número e e o
            resultado é feito a operção módulo com n.

            Args:
                message (str): mensagem que será criptografada.
                file: refere-se ao arquivo onde está salvo a chave pública.

            Retuns:
                encrypted (str): string referente a mensagem criptografada.
            """
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

    def decrypt(n, pk, encry_message):
        """
            A mensagem (string) criptografada é divida por espaçamento e inserida na lista.
            Para cada caracter é feita uma exponenciação modular onde pk é a chave privada
            e n é a multiplicação de p e q.

            Args:
                n (int): n que é gerado de acordo com p e q
                pk (int): d da chave privada
                encry_message (str): mensagem criptografada

            Retuns:
                message (str): mensagem descriptografada

        """
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
            for c in range(2):
                tmp = chr(int_blocks[i] % 1000) + tmp
                int_blocks[i] //= 1000
            message += tmp

        return message