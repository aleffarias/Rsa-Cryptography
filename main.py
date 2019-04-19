from rsa import Rsa

print('\n\t* RSA ALGORITHM *')

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
        print('\nLendo a chave pública no arquivo public_keys.txt...\nCriptografando a menssagem...')
        Rsa.encrypt(message)

    elif (option == '3'):
        encry_message = input('Digite ou copie a mensagem que será descriptografada separada por , e sem []\nExemplo: [10, 20, 30] -> 10, 11, 30\n')

        print('Lendo a chave privada no arquivo private_keys.txt...')
        print('\nMenssagem descriptografada: ', Rsa.decrypt(check, encry_message))

    elif (option == '0'):
        exit()