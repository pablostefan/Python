A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
delta = (B ** 2) - (4 * A * C)

if delta <= 0 or A == 0:
    print(f'Impossivel calcular')
else:
    raiz1 = (- B + (delta ** 0.5)) / (2 * A)
    raiz2 = (- B - (delta ** 0.5))/ (2 * A)
    print(f'R1 = {raiz1:.5f}\nR2 = {raiz2:.5f}')
