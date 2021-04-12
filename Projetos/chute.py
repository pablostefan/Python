from random import randint
num = randint(1,10)

def veirificar(valor): 
    try:
        int(valor)
    except:
        return False
    return True

while True:
    chute = input('Chute um valor\ns = SAIR\n')
    
    if chute == 's': break

    if veirificar(chute):
        chute = int(chute)
        if chute > num:
            print('Numero maior')
        if chute < num:
            print ('Numero menor')
        if chute == num:
            print ('Acertou')
            break
'''
Colocar uma regua
historico do chute
avisar que o numero está fora
'''