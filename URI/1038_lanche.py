cod, qunt = input().split()
itens = [4.00, 4.50, 5.00, 2.00, 1.50]
cod = int(cod) - 1
qunt = int(qunt)
print('Total: R$ %.2f' % (itens[cod] * qunt))