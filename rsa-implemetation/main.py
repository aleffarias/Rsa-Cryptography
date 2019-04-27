from rsa import Rsa
import os

print('\n\t* RSA ALGORITHM *')

try:
    os.mkdir('./files')
except OSError:
    pass

while True:
    option = input('\nEscolha uma opção:\n(1) - Gerar chaves\n(2) - Criptografar\n(3) - Descriptografar\n(0) - Sair\n')
    if (option == '1'):
        generate_key = input('\nDeseja gerar a chave púbica e a chave privada automaticamente?\n(1) Sim - Gerar automaticamente\n(2) Não - Digitar as chaves\n')
        if (generate_key == '1'):
            print('\nGerando as chaves...')
            Rsa.setup(1)
        elif (generate_key == '2'):
            Rsa.setup(2)
        else:
            print('Erro! Opção Inválida.\n')

    elif (option == '2'):
        message = input('Digite a mensagem que será criptografada!\n')
        print('\nLendo a chave pública no arquivo /files/public_keys.txt...\nCriptografando a menssagem...')
        Rsa.encrypt(message)

    elif (option == '3'):
        check = int(input('\nDeseja adicionar a chave privada?\n(1) Sim - Para digitar a chave privada\n(2) Não - Usa a ultima chave que foi gerada na opçao (1) - Gerar chave\n'))
        if check == 1:
            n = int(input('Digite o valor de n: '))
            pk = int(input('Digite o valor de d (chave privada): '))
        else:
            n, pk = 0, 0
        encry_message = input('Digite ou copie a mensagem que será descriptografada separada por espaçamentos\nExemplo: 10 11 30 47\n\n')

        print('\nLendo a chave privada no arquivo /files/private_keys.txt...')
        print('\nMenssagem descriptografada:', Rsa.decrypt(n, pk, encry_message))

    elif (option == '0'):
        exit()