ntermo = int(input(f'Numero de termos\n'))

def fatorial(num):
    if num != 0:
        return fatorial((num-1)) * num
    else:
        return 1

def neperiano(num):
    if num == 0:
        return 1
    else:
        return (1/fatorial(num)) + neperiano(num - 1)

print(neperiano(ntermo))