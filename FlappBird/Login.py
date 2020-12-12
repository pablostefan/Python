from typing import Text
lista = ()

with open('texto.txt', 'a+') as usuarios:
    usuario = input(f'Nome\n')
    senha = input(f'Digite a senha\n')
    user = (usuario + " ", senha + " \n")
    print(user)
    usuarios.writelines(user)

    for linha in usuarios:
        lista = linha.split()
    
    print(lista)