inicio, final = input().split()
inicio =  int(inicio)
final = int(final)

lista = ''

for i in range(inicio, final + 1):
    lista = lista + str(i)

for i in range(final, inicio - 1, -1):
    lista = lista + str(i)[::-1]

print(lista)