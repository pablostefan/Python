from csv import reader
with open('lutadores.csv') as arquivos:
    leitor_csv = reader(arquivos)
    next(leitor_csv)
    for linhas in leitor_csv:
        print(f'{linhas[0]} no(a) {linhas[1]} e mede {linhas[2]} cm')

from csv import DictReader
with open('lutadores.csv') as arquivo:
    leitorcsv = DictReader(arquivo)
    for linha in leitorcsv:
        print(f"{linha['Nome']} nasceu no {linha['Pais']} e mede {linha['Altura']} cm")