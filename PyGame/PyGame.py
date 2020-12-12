import pygame # importando o pygame

pygame.init() # Iniciar o pygame

pygame.display.set_mode([300, 600]) # Iniciando a tela, passar largura e altura em um arrey
pygame.display.set_caption("Titulo da tela") # Definir titulo da tela
 #pygame.quit() # Fechar janela

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
# pygame.QUIT é o fechar tela
# Ele cira a variavel EVENT e procura nos eventos .get(), 
# se o tipo de evento for QUIT o jogo encerra

    pygame.display.update() # Atualizar tela
    

