from random import randint

while True:
    jogar = input(f'Você gostaria de jogar o dado? s-sim n-não\n')
    if jogar != "s" and jogar != "n":
        jogar = input(f'Você gostaria de jogar o dado? s-sim n-não\nDigite apenas s ou n\n')
    if jogar == 'n':
        break
    if jogar == 's':
        print(randint(1,6))
'''
Adicionar a opção escolher faixa (primeiro num, num final)
criar objeto dado
'''