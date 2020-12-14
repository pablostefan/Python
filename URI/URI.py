valor = eval(input())

div = int(valor / 100)
nota_100 = div
print(f'NOTAS:\n{nota_100} nota (s) de R$ 100.00')

valor = (valor % 100)
div = int(valor / 50)
notas_50 = div
print(f'{notas_50} nota (s) de R$ 50.00')

valor = (valor % 50)
div = int(valor / 20)
notas_20 = div
print(f'{notas_20} nota (s) de R$ 20.00')

valor = (valor % 20)
div = int(valor / 10)
notas_10 = div
print(f'{notas_10} nota (s) de R$ 10.00')

valor = (valor % 10)
div = int(valor / 5)
notas_5 = div
print(f'{notas_5} nota (s) de R$ 5.00')

valor = (valor % 5)
div = int(valor / 2)
notas_2 = div
print(f'{notas_2} nota (s) de R$ 2.00')

valor = (valor % 2)
div = int(valor / 1)
moeda_1 = div
print(f'MOEDAS:\n{moeda_1} moeda (s) de R$ 1.00')

valor = (valor % 1)
div = int(valor / 0.5)
moeda_50 = div
print(f'{moeda_50} moeda (s) de R$ 0.50')

valor = (valor % 0.5)
div = int(valor / 0.25)
moeda_25 = div
print(f'{moeda_25} moeda (s) de R$ 0.25')

valor = (valor % 0.25)
div = int(valor / 0.1)
moeda_10 = div
print(f'{moeda_10} moeda (s) de R$ 0.10')

valor = (valor % 0.1)
div = int(valor / 0.05)
moeda_5 = div
print(f'{moeda_5} moeda (s) de R$ 0.05')

div = round(valor / 0.01)
moeda_1 = div
print(f'{moeda_1} moeda (s) de R$ 0.01')