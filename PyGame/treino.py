import pygame
pygame.init()

# 1° setar a tela
display = pygame.display.set_mode([700, 400])

# 2° vamos definir o grupo a ser desenhado
gupodedesenho = pygame.sprite.Group()

# 3° vamos cria o personagem
personagem = pygame.sprite.Sprite(gupodedesenho)
personagem.image = pygame.image.load('Bird.png')
personagem.rect = pygame.Rect(325, 175, 50, 50)
personagem.image = pygame.transform.scale(personagem.image,[50, 50])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
    
    tecla = pygame.key.get_pressed()
    if tecla [pygame.K_a]:
        personagem.rect.x -= 1

    elif tecla [pygame.K_d]:
        personagem.rect.x += 1
    
    elif tecla [pygame.K_w]:
        personagem.rect.y -=1

    elif tecla [pygame.K_s]:
        personagem.rect.y +=1


    display.fill([52, 235, 131])
    gupodedesenho.draw(display)
    pygame.display.update()

    