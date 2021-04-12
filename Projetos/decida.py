from random import choice
while True:
    fala = input(f'Oque deseja perguntar? Digite n pra sair\n').split()
    
    if fala[0]=='n': break

    resposta = choice([True, False])
    
    if len(fala[0]) <= 4:
        if resposta:
            print(f'{fala[1]} sim\n')
        else:
            print(f'Não {fala[1]}\n')
    else:
        if resposta:
            print(f'{fala[0]} sim\n')
        else:
            print(f'Não {fala[0]}\n')
"""
colocar todas as respostas num arquivo
"""