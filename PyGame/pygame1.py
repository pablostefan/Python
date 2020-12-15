# Inicar tela
import pygame
pygame.init()

display = pygame.display.set_mode([700, 400])# Iniciar a tela
gameloop = True
pygame.display.set_caption("Nome do Jogo")

#grupo que sera desenhado
drawGroup = pygame.sprite.Group()

#desenhando o retangulo
guy = pygame.sprite.Sprite(drawGroup) # quando cria o sprite ja posso passar para o grupo
guy.image = pygame.image.load('Bird.png') # Adiciona img
guy.rect = pygame.Rect(100, 100, 50, 50) 
guy.image = pygame.transform.scale(guy.image, [100, 100])


def desenhar():# função para desenhar na tela
    display.fill([3, 248, 252])
    posi = [325, 175, 50, 50]
    pygame.draw.rect(display, [235, 52, 61], posi)


while gameloop:# Game Loop
    
#pygame.event.get() Retorna os eventos do usuario
    for event in pygame.event.get(): #pega cada evento da lista de eventos dos usuarios
        if event.type == pygame.QUIT: # se o evento for fechar a janela sai do jogo
            # so pode pegar o evento uma vez
            gameloop = False

        elif event.type == pygame.KEYDOWN:# Verificar se uma tecla foi apertada
            if event.type == pygame.K_e:
                print('foi')
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                print('foi tb')

    tecla = pygame.key.get_pressed()# tecla precionada
    if tecla [pygame.K_a]:
        print('foi')
        guy.rect.x -= 1
    elif tecla[pygame.K_d]:
        guy.rect.x +=1

    display.fill([3, 248, 252])
    #posi = [325, 175, 50, 50]
    #pygame.draw.rect(display, [235, 52, 61], posi)
    
    drawGroup.draw(display) # comando que desenha o grupo no display
    pygame.display.update()# Atualizar a tela
    
