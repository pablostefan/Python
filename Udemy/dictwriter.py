from csv import DictWriter
with open('senhas.csv', 'w+') as arquivo:
    cabecalho = ['Nome', 'senha']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
