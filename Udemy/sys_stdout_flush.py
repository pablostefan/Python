import time
import sys

for i in range(5):
    #sys.stdout.write("\r{}".format(str(i)))
    #sys.stdout.write(f"\r{str(i)}")
    print(i)
    time.sleep(1)

sys.stdout.write(f"\r{str(i)}")
"""
Isso foi projetado para imprimir um número a cada segundo por cinco segundos, 
mas se você o executar como está agora (dependendo do buffer padrão do sistema), 
poderá não ver nenhuma saída até que o script seja concluído e, 
de repente, você verá 0 1 2 3 4impresso para a tela.

Isso ocorre porque a saída está sendo armazenada em buffer e, 
a menos que você libere sys.stdoutum após printo outro, 
não verá a saída imediatamente. 
Remova o comentário da sys.stdout.flush()linha para ver a diferença.
"""