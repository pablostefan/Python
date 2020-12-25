import pygame
pygame.init()

display = pygame.display.set_mode([700, 400])

desenhos = pygame.sprite.Group()

desenho_personagem = pygame.sprite.Sprite(desenhos)
desenho_personagem.image = pygame.image.load("Bird.png")
desenho_personagem.rect = pygame.Rect(325, 400, 50, 50)
desenho_personagem.image = pygame.transform.scale(desenho_personagem.image, [50, 50])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()

    tecla = pygame.key.get_pressed()
    if tecla [pygame.K_w]:
        print("foi")

    display.fill([255, 255, 255])
    desenhos.draw(display)
    pygame.display.update()