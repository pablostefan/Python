import pygame
pygame.init()

# 1° setar a tela
display = pygame.display.set_mode([700, 400])

# 2° vamos definir o grupo a ser desenhado
gupodedesenho = pygame.sprite.Group()

# 3° vamos cria o personagem
personagem = pygame.sprite.Sprite(gupodedesenho)# Define o personagem e o inclui no grupo de desenho
personagem.image = pygame.image.load('Bird.png')# Define a imagem do personagem
personagem.rect = pygame.Rect(325, 175, 50, 50)# Define o tamanho
personagem.image = pygame.transform.scale(personagem.image,[50, 50])# Enquadra no tamanho

while True:
    for event in pygame.event.get():# Verifica os eventos
        if event.type == pygame.QUIT:# Fecha a tela se o evento for sair
            pygame.display.quit()
    
    tecla = pygame.key.get_pressed()# Atribui a tecla digitada
    if tecla [pygame.K_a]:
        personagem.rect.x -= 1

    elif tecla [pygame.K_d]:
        personagem.rect.x += 1
    
    elif tecla [pygame.K_w]:
        personagem.rect.y -=1

    elif tecla [pygame.K_s]:
        personagem.rect.y +=1


    display.fill([52, 235, 131])# Preenche a tela
    gupodedesenho.draw(display)# Desenha os desenhos
    pygame.display.update()# Atualiza a tela

    