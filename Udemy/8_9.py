altura, raio = input(f'Digite a altura e o raio do cilindro\n').split()
altura = int(altura)
raio = int(raio)

def volume(altura, raio):
    pi = 3.141592
    return pi * raio * raio * altura

print(volume(altura, raio))