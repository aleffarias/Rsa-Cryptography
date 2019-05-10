from rsa import Rsa

class Client(object):
    ''' Classe onde é fieta a adição, deleção e verificação dos usuários '''

    def add():
        i = 0
        while True:
            # add condição caso exista
            user = input('Digite o nome do seu usuário: ')
            password = input('Digite uma senha: ')

            print("Usuário cadastrado\n")

            f_add = open('files/users.txt', 'w')
            f_add.write(str(user) + ' | ' + str(password) + '\n')
            f_add.close()

Client.add()