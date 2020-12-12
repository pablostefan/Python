import re
with open('texto.txt', 'a+') as usuarios:
    v=usuarios.read()
    print(dict(re.findall(r'(\w+)=(.*)',v)))